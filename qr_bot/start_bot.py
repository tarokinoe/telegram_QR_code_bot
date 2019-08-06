import io
import logging
import os
import sys

from telegram.ext import (
    CommandHandler,
    Updater,
    MessageHandler,
    Filters,
)

from qr_bot import strings
from qr_bot.utils import decode_and_select


IMAGE_SIZE_LIMIT = 30 * 1024 * 1024  # 30mb


def start_handler(bot, update):
    bot.send_message(chat_id=update.message.chat_id,
                     text=strings.GREETING)


def image_handler(bot, update):
    chat_id = update.message.chat_id
    biggest_photo = update.message.photo[-1]

    file_size = biggest_photo.file_size
    if file_size > IMAGE_SIZE_LIMIT:
        bot.send_message(chat_id=chat_id, text=strings.IMAGE_TOO_BIG)
        return

    image_file = biggest_photo.get_file().download(out=io.BytesIO())

    decoded_text, new_image_file = decode_and_select(image_file)

    if new_image_file:
        bot.send_photo(
            chat_id=chat_id,
            photo=new_image_file,
        )

    if decoded_text is None:
        decoded_text = strings.QR_NOT_FOUND

    bot.send_message(chat_id=chat_id, text=decoded_text)


def start_bot():
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )

    bot_access_token = os.getenv('BOT_ACCESS_TOKEN')
    if not bot_access_token:
        print('Envirement variable BOT_ACCESS_TOKEN is not found')
        sys.exit(1)

    updater = Updater(token=bot_access_token)

    dispatcher = updater.dispatcher
    dispatcher.add_handler(
        CommandHandler('start', start_handler)
    )
    dispatcher.add_handler(
        MessageHandler(Filters.photo, image_handler)
    )

    updater.start_polling()


if __name__ == '__main__':
    start_bot()
