# Seyren Telegram Bot
===================

+ Set `SECRET_KEY` and `BOT_TOKEN` and `BOT_USERNAME` and `ALERTS_CHANNEL_ID` in settings.py
+ Build docker: docker build -t seyren-telegram-bot .
+ Run docker: docker run -i -p 0.0.0.0:14500:14500 seyren-telegram-bot
+ Set seyren HTTP notification to: http://localhost:145000/seyren/
