import PyStella

time = PyStella.pyStellaTime
stellarium = PyStella.pyStellarium
constellation = PyStella.pyStellaConstellation
location = PyStella.pyStellaLocation
request = PyStella.requestServer

time.setTimeUtc(year=2022, month=12, day=23, hour=22, minute=0, second=0)
time.setTimeRate(1)
location.set(latitude=50.27, longitude=2.89, elevation=110)
stellarium.move_altaz(azimut=90, altitude=0) # à revoir ...
stellarium.wait(pause_in_sec=5)


constellation.reset_all_property()

stellarium.set_field_of_view(60)
stellarium.set_gui_visible(True)
stellarium.select_object_by_name(object_name='orion',mode='center')

stellarium.wait(pause_in_sec=3)

constellation.set_property(linedisplayed=True, isolateselected=True)

stellarium.wait(pause_in_sec=3)
constellation.set_property(artdisplayed=True, linedisplayed=False)

stellarium.wait(pause_in_sec=3)

stellarium.select_object_by_name(object_name='canis major', mode='center')
stellarium.set_field_of_view(75)
stellarium.wait(pause_in_sec=3)

stellarium.set_gui_visible(True)
# stellarium.setFieldOfView(90)
