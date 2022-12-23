import requests


class pyStellaRequestServer:

    def __init__(self):

        self.server_url = 'http://localhost:8090'
        self.api_url = '/api/'
        self.request_url = self.server_url + self.api_url

    def post(self, service, data=None):
        try:
            r = requests.post(self.request_url + service, data)
        except:
            return None
        else:
            return r

    def get(self, service, result='json'):
        try:
            r = requests.get(self.request_url + service)
            return r.json() if (result == 'json') else r.text
        except:
            return None
