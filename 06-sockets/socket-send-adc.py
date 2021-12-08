from machine import Pin, ADC
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

# preparations for ADC input
pot = ADC(Pin(36))             # on most boards, pin 36 is ADC0 
pot.atten(ADC.ATTN_11DB)       # Full range: 3.3v
pot.width(ADC.WIDTH_12BIT)     # set 9 bit return values (returned range 0-511)

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
    
    # read the potentiometer and store its' value
    pot_value = pot.read()
    
    # send the value to the server
    sendData(str(pot_value))
    print("sending : ", pot_value)   
        
    # tiny delay
    sleep(.01)

