from utime import sleep
from machine import Pin

led = Pin(32,Pin.OUT)

while True:
    led.value(1)
    sleep(0.5)
    led.value(0)
    sleep(0.5)

