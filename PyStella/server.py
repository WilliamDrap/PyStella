import requests
from datetime import datetime
from PyStella.timeServer  import pyStellaMasterTime
from PyStella.requestServer import pyStellaRequestServer

class pyStellaServer:

    def __init__(self,request_server):
        self.requestServer = request_server

    def setFiedOfView(self,fov=45):
        r = self.requestServer.post('main/fov',{'fov': str(fov)})
    
    def setGUIVisible(self,gui_visible=True):
        r = self.requestServer.post('stelproperty/set',{'id':'StelGui.visible','value':str(gui_visible)})

    def selectObjectByName(self,object_name,mode='center'): # mode = 'center' par défaut ou 'zoom'
        r = self.requestServer.post('main/focus',{'target': object_name,'mode': mode})