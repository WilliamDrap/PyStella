import PyStella
#import pyautogui
#from PIL import Image

time = PyStella.pyStellaTime
stellarium = PyStella.pyStellarium
constellation = PyStella.pyStellaConstellation
location = PyStella.pyStellaLocation
request = PyStella.requestServer

constellation.reset_all_property()

time.setTimeUtc(year=2022, month=12, day=23, hour=21, minute=0, second=0)
time.setTimeRate(1)
location.set(latitude=50.27, longitude=2.89, elevation=110)
stellarium.set_field_of_view(90)
stellarium.move_altaz(azimut=135, altitude=40).wait(3)

stellarium.set_gui_visible(False)
stellarium.select_object_by_name(object_name='orion', mode='center')

stellarium.wait(pause_in_sec=4)

constellation.set_property(linedisplayed=True, isolateselected=True)

stellarium.wait(pause_in_sec=3)
constellation.set_property(artdisplayed=True, linedisplayed=False)

stellarium.wait(pause_in_sec=3)

stellarium.select_object_by_name(object_name='canis major', mode='mark')
#stellarium.set_field_of_view(75)
# im1=pyautogui.screenshot('stellarium.png')
stellarium.wait(pause_in_sec=3)
constellation.set_property(artdisplayed=False, linedisplayed=False)
stellarium.select_object_by_name(object_name='m42', mode='center')
stellarium.set_field_of_view(3.8)
stellarium.wait(pause_in_sec=10)

stellarium.set_gui_visible(True)
# stellarium.setFieldOfView(90)
#im1.show()
