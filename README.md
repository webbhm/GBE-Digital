# GBE-Digital
Developing a digital version of the Growing Beyond Earth grow box
This project takes the Fairchild Gardens [Growing Behond Earth](https://fairchildgarden.org/science-and-education/science/growing-beyond-earth/)  grow box and enhances it by adding a Raspberry Pi to replace the current manual light controller and the stand-alone temperature/humidity sensor.

The following is the working hypothesis under development.

## Hardware
1) Raspberry Pi Zero for control
2) [BME280](https://www.amazon.com/BME280/s?k=BME280) I2C sensor (temperature, humidity, pressure)
3) Screen - [this](https://www.amazon.com/gp/product/B07D83DY17/ref=ppx_yo_dt_b_asin_title_o02_s00?ie=UTF8&psc=1) or[this](https://www.adafruit.com/product/4506)
4) Removable USB thumb drive, connnected via an OTC cable for data logging (optional)

## Software:
The software is designed to be driven by configuration files.  The system is composed of the following main sections:
1) Menu:
  a) Selecting pre-configured light settings
  b) Display options (temperature in C or F)
  c) Diagnostics
2) Sensor logging:
  a) A [BME280](https://www.amazon.com/BME280/s?k=BME280) sensor provides temperature, humidity and pressure via the I2C port.
  b) Utility programs read the sensor and write data to a file on the USB drive.
3) Light Management:
  a) GrowLight is the main class that interfaces with the LED panel.  A helper file is used to configure standard settings and control on/off behavior.
  b) Since the PWM control must be on 7/24 (unmanaged GPIO pins can produce strange behavior), the GrowLight is made into a service.
4) Service:
  a) A socket, along with systemd is used to wrapper the light in a service.  TCP is used to communicate and control the light.  To make the service generic, command handling is in a separate helper class.  Wait; isn't TCP/IP an internet protocol, and the GBE-Digital is not connected to the internet?  Well, yes and no.  TCP can be use to communicate within a computer, or (with a few setting changes) be a communication between devices over the internet.  Here it is used for communication between processes on the Pi Zero, but change some settings, connect to a router, open a router for port forwarding and add a reverse proxy server for security (ie. [nginx](https://www.nginx.com/)) and you can turn the GBE-Digital into an IOT device; not only to control lights but to retreive sensor readings and pictures.
 b) There is a small client that sends messages via TCP to the service.
3) Sensor reading and logging

I have worked through most of the software problems (dynamic menu, lights as a software daemon service), and now need to integrate the software parts and the hardware (some of which will be coming this week).  Hopefully I will have something up and running in the next few weeks.  Proxy objects (simplified stand-ins for the real objects) are in the /test directory.  These are files I used during development that are useful for testing low level functions.  Completed production files are in /python.  These should be copied to /home/pi/python on the Raspberry Pi Zero.

This should match the current features of the GBE box, and add a few more.  It also opens up a lot of new options and hacking opportunities.  It just begs for a camera.  More sensors would not be an issue. We do not plan on cloud access (school wifi is too much of a pain point at this time), but for those who know how, it is an easy addition.  With lights as a service (and a generic socket), the lights (or anything else in the box) could be controlled over wifi with a slight modification to the socket address, opening a router port and getting a reverse proxy for web security ([nginx](https://www.nginx.com/)?!).  Post processing of the logged data is another avenue.

Architecture:

Pi Zero Configuration:
* Enable VNC, SPI, I2C
* Add software package usbmount (for easy access to the flash drive)
* For deployment, the GUI can/should be turned off.
