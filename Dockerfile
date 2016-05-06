FROM    ubuntu:trusty
RUN     apt-get -y update

# Install required packages
RUN     apt-get -y install python-pip nginx
RUN     pip install django==1.8.13 gunicorn==19.4.5 supervisor==3.2.3 requests==2.10.0

# Add SeyrenTelegramBot to /app
ADD     . /app/SeyrenTelegramBot/
RUN     cd /app/SeyrenTelegramBot/ && python manage.py migrate
RUN     cd /app/SeyrenTelegramBot/ && echo yes | python manage.py collectstatic
RUN     cd /app/SeyrenTelegramBot/ && python manage.py initialize_admin

# Link supervisor configs
RUN     cp /app/SeyrenTelegramBot/conf/supervisor/supervisord.conf /etc/supervisord.conf
RUN     ln -s /app/SeyrenTelegramBot/conf/supervisor/programs /etc/supervisor
RUN     ln -s /app/SeyrenTelegramBot/conf/nginx/sites/seyren-telegram-bot /etc/nginx/sites-enabled/
RUN     rm /etc/nginx/sites-enabled/default

# Admin Interface
EXPOSE  :8035

# Seyren Interface
EXPOSE  :14500


CMD     ["/usr/local/bin/supervisord"]
