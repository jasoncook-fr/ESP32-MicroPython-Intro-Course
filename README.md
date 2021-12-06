## Getting started with Micropython on ESP32

### To follow the examples it is recommended to install Thonny (Python IDE for beginners)

For download instructions, visit [The official website](https://thonny.org "Official Thonny Website")

### Install Firmware onto the ESP32

1. **Download esptool software** <br />

```shell

git clone https://github.com/espressif/esptool.git

```

2. **Download the Necessary Firmware** <br />
Visit the [download page](https://micropython.org/download/) of the official micropython website. <br />
You will notice there are many options. For most generic ESP32 devices the following firmware profile should be fine: [here](https://micropython.org/download/esp32/)

Using wget in commandline:

```shell

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



