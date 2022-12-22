import PyStella
from time import sleep


time        = PyStella.pyStellaTime
stellarium  = PyStella.pyStellarium
request     = PyStella.requestServer

r = request.post('simbad/lookup',{"str":"HD51593"})
print(r.text)