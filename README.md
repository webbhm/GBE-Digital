# GBE-Digital
Developing a digital version of the Growing Beyond Earth grow box
This project takes the Fairchild Gardens [Growing Behond Earth](https://fairchildgarden.org/science-and-education/science/growing-beyond-earth/)  grow box and enhances it by adding a Raspberry Pi to replace the current manual light controller and the stand-alone temperature/humidity sensor.

The following is the working hypothesis under development.

Hardware
1) Raspberry Pi Zero for control
2) [BME280](https://www.amazon.com/BME280/s?k=BME280) I2C sensor (temperature, humidity, pressure)
3) Screen - [this](https://www.amazon.com/gp/product/B07D83DY17/ref=ppx_yo_dt_b_asin_title_o02_s00?ie=UTF8&psc=1) or[this](https://www.adafruit.com/product/4506)
4) Removable USB thumb drive for data logging (optional)

Software:
1) Screen menu for:
  a) Selecting pre-configured light settings
  b) Display options (temperature in C or F)
  c) Diagnostics
2) Sensor logging and display
3) Temperature and Humidity display (replace current temp/humidity sensor)

I have worked through most of the software problems (dynamic menu, lights as a software daemon service), and now need to integrate the software parts and the hardware (some of which will be coming this week).  Hopefully I will have something up and running in the next few weeks.

This should match the current features, and add a few more.  It also opens up a lot of new options and hacking opportunities.  It just begs for a camera.  More sensors would not be an issue. We do not plan on cloud access (school wifi is too much of a pain point at this time), but for those who know how, it is an easy addition.  With lights as a service (and a generic socket), the lights (or anything else in the box) could be controlled over wifi with a slight modification to the socket address, opening a router port and getting a reverse proxy for web security (nginx?!).  Post processing of the logged data is another avenue.
