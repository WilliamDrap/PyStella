import PyStella
from time import sleep

time = PyStella.pyStellaTime
stellarium = PyStella.pyStellarium
constellation = PyStella.pyStellaConstellation
request = PyStella.requestServer

constellation.reset()

stellarium.setFieldOfView(60)
stellarium.setGUIVisible(False)
time.setTimeUtc(2022, 9, 14, 21, 10, 0)
stellarium.selectObjectByName(object_name='uranus', mode='zoom')
stellarium.setFieldOfView(fov=0.5)
time.setTimeRate(30)

stellarium.setGUIVisible(True)
# stellarium.setFieldOfView(90)
