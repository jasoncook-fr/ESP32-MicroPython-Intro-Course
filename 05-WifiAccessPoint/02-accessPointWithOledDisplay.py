from machine import Pin, SoftI2C
import ssd1306
from utime import sleep
import network
import gc
#garbage collect is common protocol
gc.collect()

# Prepare oled display 
oled_width = 128
oled_height = 32
i2c = SoftI2C(scl=Pin(22), sda=Pin(21))
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

# change network name and password to your choosing
ssid = 'MCU'
password = '12345'

# Make our device a wireless access-point
ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid=ssid, password=password)

#wait until access point is ready
while ap.active() == False:
    pass

print('Connection successful')

# get our ip address
ip_address = list(ap.ifconfig())

# print access-point info to the oled screen
oled.text('SSID:', 0, 0)
oled.text(ssid, 42, 0)
oled.text('IP:', 0, 20)
oled.text(ip_address[0], 25, 20)
oled.show()
