Telegram bot. Can read QR code.  
https://telegram.me/BarQRCodeBot

### Installing
1. Download source code
    ```
   git clone https://github.com/tarokinoe/telegram_QR_code_bot.git qr_bot
   cd qr_bot
   ``` 
2. Register telegram bot [here](https://telegram.me/botfather) 
3. Create file env.list and put there bot access token  
   env.list 
   ```
   BOT_ACCESS_TOKEN=<bot access token>
   ```
4. Build docker image   
   ```
   docker build -t qrbot .   
   ```
5. Launch
   ```
   docker run -d --env-file ./env.list qrbot
   ```