import PyStella
from time import sleep

time = PyStella.pyStellaTime
stellarium = PyStella.pyStellarium
constellation = PyStella.pyStellaConstellation
request = PyStella.requestServer

constellation.reset_all_property()

time.setTimeUtc(2022, 12, 23, 22, 0, 0)
stellarium.set_field_of_view(60)
stellarium.set_gui_visible(False)
stellarium.select_object_by_name(object_name='orion')

sleep(3)

constellation.set_property(linedisplayed=True, isolateselected=True)

sleep(3)
constellation.set_property(artdisplayed=True, linedisplayed=False)
sleep(3)
stellarium.select_object_by_name(object_name='canis major', mode='center')

time.setTimeRate(1)
sleep(3)

stellarium.set_gui_visible(True)
# stellarium.setFieldOfView(90)
