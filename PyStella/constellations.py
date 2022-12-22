class pyStellaConstellationClass:

    def __init__(self, request_server=None):
        self.requestServer = request_server
        self.line_displayed = False
        self.art_displayed = False
        self.isolate_selected = False

    def reset_property(self):
        self.set_property(False,False,False)

    def lineDisplayed(self, displayed=False):
        r = self.requestServer.post('stelproperty/set',
                                    {"id": "ConstellationMgr.linesDisplayed", "value": str(displayed)})

    def artDisplayed(self, displayed=False):
        r = self.requestServer.post('stelproperty/set',
                                    {"id": "ConstellationMgr.artDisplayed", "value": str(displayed)})

    def isolateSelected(self, isolated=False):
        r = self.requestServer.post('stelproperty/set',
                                    {"id": "ConstellationMgr.isolateSelected", "value": str(isolated)})

    def set_property(self, linedisplayed=None, artdisplayed=None, isolateselected=None):

        if self.isolate_selected is not None:
            self.isolateSelected(isolateselected)
            self.isolate_selected = isolateselected
        if linedisplayed is not None:
            self.line_displayed = linedisplayed
            self.lineDisplayed(linedisplayed)
        if artdisplayed is not None:
            self.artDisplayed(artdisplayed)
            self.art_displayed = artdisplayed

