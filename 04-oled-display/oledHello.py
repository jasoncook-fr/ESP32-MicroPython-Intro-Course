from machine import Pin, SoftI2C
import ssd1306
from utime import sleep

# I2C Pin assignment 
i2c = SoftI2C(scl=Pin(22), sda=Pin(21))

# larger display is 128x64. Smaller display is 128x32 
oled_width = 128
oled_height = 32

oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

oled.text('This is a test', 0, 0)
oled.text('This is test 2!', 0, 12)
oled.text('Is this test 3?', 0, 24)
