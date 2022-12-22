import requests

class pyStellaRequestServer:
  
    def __init__(self):

        self.server_url  = 'http://localhost:8090'
        self.api_url     = '/api/'  
        self.request_url = self.server_url + self.api_url

    def post(self,service,data=None):
        try:
            r = requests.post(self.request_url+service,data)
            return r
        except:
            return None
    
    def get(self,service):
        try:
            r = requests.get(self.request_url+service)
            return r.json()
        except:
            return None

