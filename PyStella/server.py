import requests
from datetime import datetime
from PyStella.timeServer import pyStellaMasterTime
from PyStella.requestServer import pyStellaRequestServer


class pyStellaServer:

    def __init__(self, request_server):
        self.requestServer = request_server

    def set_field_of_view(self, fov=45):
        r = self.requestServer.post('main/fov', {'fov': str(fov)})

    def set_gui_visible(self, gui_visible=True):
        r = self.requestServer.post('stelproperty/set', {'id': 'StelGui.visible', 'value': str(gui_visible)})

    def select_object_by_name(self, object_name=None, mode='mark'):  # mode = 'center' par défaut ou 'zoom'
        r = self.requestServer.post('main/focus', {'target': object_name, 'mode': mode})

