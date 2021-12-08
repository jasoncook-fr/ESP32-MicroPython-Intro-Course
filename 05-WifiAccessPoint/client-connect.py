'''
This code is to be run on a second ESP32 device (client device).
This illustrates simple connection requirements. No data is sent or received.
'''
import network
import utime
import gc
gc.collect()

# change network name and password to match that of your end-device
ssid = 'MCU'
password = '12345'

station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(ssid)

while station.isconnected() == False:
    print(station.isconnected())
    utime.sleep(.01)
    pass

print('Connection successful')
print(station.ifconfig())
