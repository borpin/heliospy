# Helios RS-485 Communication Library

## Introduction

I found the code to communicate with the Helios RS-485 bus via a USB interface from here. [SmartHome.py](http://mknx.github.io/smarthome/).

I currently have it running for my Helios EC500 PRO using the USB-RS485 Interface on an Orange Pi Zero.

## From the source documentation
### Supported functions:

* Reading temperature values
* Turn ventilation system on/off
* Switching between summer/winter mode (bypass)
* Read/Write fan speed
* Read/Write bypass temperature
* Read/Write maximum/minimum fan speed.

Values will be read periodically from the ventilation system.

Using this plug in as a command line tool (Python module argparse required).

# Improvements

I need to improve the controlling script.  Pretty rubbish (though it does work).

Feel free to clone and improve :)
