import PyStella
from time import sleep

time = PyStella.pyStellaTime
stellarium = PyStella.pyStellarium
constellation = PyStella.pyStellaConstellation
request = PyStella.requestServer

constellation.reset()

stellarium.setFiedOfView(60)
stellarium.setGUIVisible(False)
time.setTimeUtc(2022, 12, 21, 20, 0, 0)
stellarium.selectObjectByName(object_name='orion')
sleep(3)
time.setTimeRate(5)  # 1sec = 10sec
constellation.isolateSelected(True)
constellation.lineDisplayed(True)
sleep(3)
constellation.artDisplayed(True)
sleep(3)
stellarium.selectObjectByName(object_name='betelgeuse', mode='zoom')
sleep(3)
stellarium.selectObjectByName(object_name='M42', mode='center')
sleep(2)
stellarium.setFiedOfView(1)
sleep(5)
stellarium.setGUIVisible(True)
stellarium.setFiedOfView(90)
