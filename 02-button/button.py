'''
Basic Button example
--------------------
Internal pull-up resistor is used in the code for the pushbutton.
Thus pull-up resistor is not required on the breadboard.
'''

from machine import Pin
from utime import sleep

# create output pin on GPIO22
led = Pin(22, Pin.OUT)    

# create input pin on GPIO21 and enable internal pull-up resistor
button = Pin(21, Pin.IN, Pin.PULL_UP)

while True:
    # read button state and store the value
    buttonState = button.value()
    
    # print the result of the push button state
    print(buttonState)
    # add a tiny delay to buffer the print function
    sleep(.01)
    
    # turn on the led if button is pushed
    if buttonState is 0:
        led.value(1)
        
    # turn off the led by default    
    else:
        led.value(0)

