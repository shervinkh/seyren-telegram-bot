import requests


def escape_markdown(str):
    str = str.replace('*', '\\*')
    str = str.replace('_', '\\_')
    str = str.replace('[', '\\[')
    return str


class Bot(object):
    def __init__(self, token):
        self.token = token

    def call_remote_method(self, method, parameters):
        url = 'https://api.telegram.org/bot{token}/{method}'.format(token=self.token,
                                                                    method=method)
        return requests.post(url, json=parameters)

    def send_message(self, id, text):
        parameters = {'chat_id': id, 'text': text, 'parse_mode': 'Markdown',
                      'disable_web_page_preview': True}
        return self.call_remote_method('sendMessage', parameters)

