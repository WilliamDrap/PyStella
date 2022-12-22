class pyStellaConstellationClass:

    def __init__(self, request_server=None):
        self.requestServer = request_server

    def reset(self):
        self.artDisplayed(False)
        self.lineDisplayed(False)

    def lineDisplayed(self, displayed=False):
        r = self.requestServer.post('stelproperty/set',
                                    {"id": "ConstellationMgr.linesDisplayed", "value": str(displayed)})

    def artDisplayed(self, displayed=False):
        r = self.requestServer.post('stelproperty/set',
                                    {"id": "ConstellationMgr.artDisplayed", "value": str(displayed)})

    def isolateSelected(self, isolated=False):
        r = self.requestServer.post('stelproperty/set',
                                    {"id": "ConstellationMgr.isolateSelected", "value": str(isolated)})
