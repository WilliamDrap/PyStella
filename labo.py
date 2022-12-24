import PyStella
from time import sleep


time        = PyStella.pyStellaTime
stellarium  = PyStella.pyStellarium
request     = PyStella.requestServer

r = request.get('simbad/lookup',{"str":"HD51593"})
print(r)