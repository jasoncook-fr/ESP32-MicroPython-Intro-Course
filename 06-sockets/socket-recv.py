from machine import Pin
import usocket as socket
import network
import gc

# common practice to use garbage collect
gc.collect()

# our wireless name and password
SSID = 'MCU'
PASSWORD = '12345'

# Socket port number
PORT = 8080

# create output pin on GPIO5
led = Pin(5, Pin.OUT)

# activate network and create access point
ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid=SSID, password=PASSWORD)

while ap.active() == False:
  pass

print('Connection successful')
print(ap.ifconfig())

# Setup our socket
# Bind to all interfaces. Server accessible to other hosts!
SOCK = socket.socket()
ai = socket.getaddrinfo("0.0.0.0", PORT)
addr = ai[0][-1]
SOCK.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
SOCK.bind(addr)
SOCK.listen(5)

print("Listening")

while True:
    # wait for data to be received
    res = SOCK.accept()
    client_sock = res[0]
    
    # print received data
    print("Received:")
    req = client_sock.read()
    print("raw : ", req)
    BUF = req.decode('utf-8')
    print("decoded : ", BUF)

    client_sock.close()
    print()
    
    #Turn LED on or off
    led.value(int(BUF))



