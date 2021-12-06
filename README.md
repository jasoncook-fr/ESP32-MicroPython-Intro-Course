## Getting started with Micropython on ESP32

### In this repository are included examples as follows <br/>

| IO Function         | Exercise                               |
|---------------------|----------------------------------------|
| OUTPUT              | Blink a LED                            |
| INPUT               | add a push-button                      |
| INPUT & OUTPUT      | sequence 3 LEDs at push of a button    |
| ADC                 | add a potentiometer for analog input   |
| PWM                 | create varied luminosity of a LED      |
| PWM                 | automated control of a Servo motor     |
| PWM & ADC           | control a Servo motor with analog input|

<br />

### To follow the examples it is recommended to install Thonny (Python IDE for beginners)

For download instructions, visit [The official website](https://thonny.org "Official Thonny Website")

__Thonny Screenshot__

![Thonny-preview](images/thonny.png)
<br />

### Install Firmware onto the ESP32

1. Visit the [download page](https://micropython.org/download/) of the official micropython website. <br />
**You will notice there are many options. For most generic ESP32 devices the following firmware profile should be fine: [Here](https://micropython.org/download/esp32/)**

2. While pressing the _BOOTSEL_ button on the Raspberry Pico, connect it to your computer with a micro-USB cable.

3. The Raspberry Pico will appear as a USB storage device on your computer.

4. Drag and drop the downloaded file onto the mounted Raspberry device.

__Illustration from the raspberry website:__

![install-firmware](images/install-firmware.webp)

<br />

### Raspberry Pico Pinout is as follows:

![Pico-Pinout](images/pico_pinout.png)
