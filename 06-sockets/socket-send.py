from machine import Pin
from utime import sleep
import network
import socket
import gc
gc.collect()

# wireless name and password
SSID = 'MCU'
PASSWORD = '12345'

#socket values
SRV_ADDR = "192.168.4.1"
PORT = 8080

# create input pin for push-button
button = Pin(15, Pin.IN, Pin.PULL_UP)

# activate network and connect to access point
station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(SSID)

while station.isconnected() == False:
    pass

print('Connection successful')
print(station.ifconfig())

# Function to manage sending socket data
def sendData(data):
    SOCK = socket.socket()
    addr = socket.getaddrinfo(SRV_ADDR, PORT)[0][-1]
    SOCK.connect(addr)
    SOCK.write(str(data))
    SOCK.close()

# boolean flag for our button
buttonFlag = True

while True:
    # read the value of our push-button
    buttonState = button.value()
    
    if buttonState is 0 and buttonFlag is True:
        print("Sending : ", buttonState)
        sendData(str(buttonState))
        buttonFlag = False
        
    elif buttonState is 1 and buttonFlag is False:
        print("Sending : ", buttonState)
        sendData(str(buttonState))
        buttonFlag = True
        
    # tiny delay
    sleep(.01)

