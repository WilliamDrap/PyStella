import PyStella
from time import sleep

time = PyStella.pyStellaTime
stellarium = PyStella.pyStellarium
constellation = PyStella.pyStellaConstellation
request = PyStella.requestServer

constellation.reset_property()
request.post('http://localhost:8090/api/main/focus')
print(constellation.isolate_selected)
time.setTimeNow()
stellarium.setFieldOfView(60)
stellarium.setGUIVisible(False)
stellarium.selectObjectByName(object_name='orion')

sleep(3)

constellation.set_property(
    linedisplayed=True,
    isolateselected=True
)
sleep(3)
constellation.set_property(
    artdisplayed=True,
    linedisplayed=False
)
sleep(3)
stellarium.selectObjectByName(object_name='canis minor', mode='mark')
sleep(3)

stellarium.setGUIVisible(True)
# stellarium.setFieldOfView(90)
