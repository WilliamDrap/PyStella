import PyStella
from time import sleep

time = PyStella.pyStellaTime
stellarium = PyStella.pyStellarium
constellation = PyStella.pyStellaConstellation
location = PyStella.pyStellaLocation
request = PyStella.requestServer

time.setTimeUtc(year=2022, month=12, day=23, hour=22, minute=0, second=0)
time.setTimeRate(1)
location.set(latitude=50.27, longitude=2.89, elevation=110)
list_location = location.get_all_location()

constellation.reset_all_property()

stellarium.set_field_of_view(60)
stellarium.set_gui_visible(False)
stellarium.select_object_by_name(object_name='orion',mode='center')

sleep(3)

constellation.set_property(linedisplayed=True, isolateselected=True)

sleep(3)
constellation.set_property(artdisplayed=True, linedisplayed=False)
sleep(3)
stellarium.select_object_by_name(object_name='canis major', mode='center')
sleep(3)
stellarium.select_object_by_name(object_name='pleiades',mode='zoom')
stellarium.set_field_of_view(2.5)

stellarium.set_gui_visible(True)
# stellarium.setFieldOfView(90)
