import io

from PIL import Image, ImageDraw
from pyzbar.pyzbar import decode


def select_code_on_image(image, polygon):
    coordinates = [(p.x, p.y) for p in polygon]
    coordinates.append(coordinates[0])
    image = image.convert(mode='RGB')
    draw = ImageDraw.Draw(image)
    draw.line(coordinates, fill='#00aa00', width=4)

    return image


def decode_and_select(image_file):
    decoded_text = None
    new_image_file = None

    image = Image.open(image_file)
    results = decode(image)

    if results:
        decoded_text = []
        for result in results:
            image = select_code_on_image(image, result.polygon)
            decoded_text.append(result.data.decode())

        new_image_file = io.BytesIO()
        image.save(new_image_file, format='PNG')
        new_image_file.seek(0)
        decoded_text = '\n'.join(decoded_text)

    return decoded_text, new_image_file
