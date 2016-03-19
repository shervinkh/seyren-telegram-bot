FROM    ubuntu:trusty
RUN     apt-get -y update

# Install required packages
RUN     apt-get -y install python-pip
RUN     pip install django==1.8.10 gunicorn==19.4.5 supervisor==3.2.2 requests==2.9.1

# Add SeyrenTelegramBot to /app
ADD     . /app/SeyrenTelegramBot/
RUN     cd /app/SeyrenTelegramBot/ && python manage.py migrate

# Link supervisor configs
RUN     cp /app/SeyrenTelegramBot/conf/supervisor/supervisord.conf /etc/supervisord.conf
RUN     ln -s /app/SeyrenTelegramBot/conf/supervisor/programs /etc/supervisor


# Seyren Telegram Bot
EXPOSE  :14500


CMD     ["/usr/local/bin/supervisord"]
