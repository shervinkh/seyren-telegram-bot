# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alert',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text=b'A short description for this alert.', max_length=128, verbose_name=b'Name')),
                ('url', models.CharField(help_text=b'If you set this to x, you should send seyren alerts to http://my_address/seyren/x/', max_length=128, verbose_name=b'Url', db_index=True)),
                ('bot_token', models.CharField(help_text=b'The token of the bot you want to send alerts from.', max_length=128, verbose_name=b'Bot Token')),
                ('chat_id', models.CharField(help_text=b'The chat id you want to send the alert to. This could be either user id, group id, or channel username (Starting with @)', max_length=128, verbose_name=b'Chat ID')),
            ],
        ),
    ]
