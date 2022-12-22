from PyStella.server import pyStellaServer
from PyStella.requestServer import pyStellaRequestServer
from PyStella.timeServer import pyStellaMasterTime
from PyStella.constellations import pyStellaConstellationClass

requestServer = pyStellaRequestServer()

pyStellaTime = pyStellaMasterTime(requestServer)
pyStellaTime.getStellariumTime()
pyStellaTime.setTimeRate(1)

pyStellarium = pyStellaServer(requestServer)
pyStellaConstellation = pyStellaConstellationClass(requestServer)
