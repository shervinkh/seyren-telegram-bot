from django.db import models


class Alert(models.Model):
    name = models.CharField(null=False, verbose_name='Name', max_length=128,
                            help_text='A short description for this alert.')

    url = models.CharField(null=False, verbose_name='Url', max_length=128, db_index=True,
                           help_text='If you set this to x, you should send '
                                     'seyren alerts to http://my_address/seyren/x/')

    bot_token = models.CharField(null=False, verbose_name='Bot Token', max_length=128,
                                 help_text='The token of the bot you want to send alerts from.')

    chat_id = models.CharField(null=False, verbose_name='Chat ID', max_length=128,
                               help_text='The chat id you want to send the alert to. This could be '
                                         'either user id, group id, or channel username (Starting with @)')
