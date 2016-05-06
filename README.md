# Seyren Telegram Bot
===================

+ Set `SECRET_KEY` in settings.py
+ Build docker: docker build -t seyren-telegram-bot ./
+ Run docker: docker run -i -p 0.0.0.0:14500:14500 -p 0.0.0.0:8035:8035 seyren-telegram-bot
+ Set seyren HTTP notification to: http://localhost:145000/seyren/alert_url/ (Set alert_url in admin)
+ Visit admin at http://localhost:8035/admin with (Username=admin, Password=admin by default)
