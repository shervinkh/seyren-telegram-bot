from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseBadRequest
from django.conf import settings

from bot_utils.bot import bot, escape_markdown

from datetime import datetime
import json

state_to_str = {'OK': 'Back To OK',
                'WARN': 'Warning',
                'ERROR': 'Error'}


@csrf_exempt
def seyren_notification(request):
    if request.method != 'POST':
        return HttpResponseForbidden()

    try:
        notification = json.loads(request.body)

        from_type = notification['alerts'][0]['fromType']
        to_type = notification['alerts'][0]['toType']
        value = notification['alerts'][0]['value']
        warn = notification['alerts'][0]['warn']
        error = notification['alerts'][0]['error']
        timestamp = notification['alerts'][0]['timestamp']
        time_str = datetime.fromtimestamp(timestamp/1000.0).strftime('%Y/%m/%d %H:%M:%S')
        checkId = notification['alerts'][0]['checkId']
        target = notification['alerts'][0]['target']
        name = notification['check']['name']
        seyrenUrl = notification['seyrenUrl']

        name = escape_markdown(name)
        target = escape_markdown(target)

        title = '%s - %s' % (name, state_to_str[to_type])
        url = '%s/#/checks/%s' % (seyrenUrl, checkId)

        message = '*{title}*\n' \
                  '*Target:* {target}\n' \
                  '*Value:* {value}\n' \
                  '*From State:* {from_t}\n' \
                  '*To State:* {to}\n' \
                  '*Time:* {time}\n' \
                  '*Warn Level:* {warn}\n' \
                  '*Error Level:* {error}\n' \
                  '\n' \
                  'Alerts by [Seyren]({url}) via @{username}'

        message = message.format(title=title, target=target, value=value, from_t=from_type,
                                 to=to_type, time=time_str, warn=warn, error=error, url=url,
                                 username=settings.BOT_USERNAME)

        bot.send_message(settings.ALERTS_CHANNEL_ID, message)
        return HttpResponse(status=204)
    except Exception:
        return HttpResponseBadRequest()
