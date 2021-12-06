# Getting started with Micropython on ESP32

### To follow the examples it is recommended to install Thonny (Python IDE for beginners)

For download instructions, visit [The official website](https://thonny.org "Official Thonny Website")

## Install Firmware onto the ESP32

**Download the esptool software**

```shell

git clone https://github.com/espressif/esptool.git

```

**Download the necessary firmware for our board**
Visit the official micropython [download page](https://micropython.org/download/). <br />
You will notice there are many options. For most generic ESP32 devices try [this one](https://micropython.org/download/esp32/) .

Alternatively we can use wget in commandline:

```shell

# all following commands to be executed in the esptool folder

cd esptool

wget https://micropython.org/resources/firmware/esp32-20210902-v1.17.bin


```

Erase anything currently on the ESP32:

```shell

esptool.py --chip esp32 --port /dev/ttyUSB0 erase_flash

```
program the firmware starting at address 0x1000:

```shell

esptool.py --chip esp32 --port /dev/ttyUSB0 --baud 460800 write_flash -z 0x1000 esp32-20190125-v1.10.bin

```

3. Connect the ESP32 to your computer with a micro-USB cable.



