# Libraries
This repository contains _**links**_ to various libraries that are used to support functions and features of the EnvidoDIY Mayfly Data Logger board.  Please note that these libraries are not maintained in this repository, but rather are independent repositories that are linked as submodules of this repository.

### How to use them:

If you are familiar with Git, clone this repo into your "MyDocuments\Arduino\libraries" folder.  Otherwise, you can download all libraries by clicking on the green "Clone or Download" button in the upper right of this window.  Select "Download ZIP" and save that file.  Uncompress the zip file into your "MyDocuments\Arduino\libraries" folder.  The libraries should then be accessible to the Arduino Software (IDE).  Each library can also be downloaded individually by clicking on that library and then downloading a ZIP of only that library.

#### These libraries are for basic components built into the EnviroDIYMayfly:
* [EnviroDIY PCInt](https://github.com/EnviroDIY/Sodaq_PcInt/) - A fork from [Sodaq](https://github.com/SodaqMoja/Sodaq_PcInt) - administrates and handles pin change interrupts on the Atmel microcontroller built into the Mayfly.
* [Adafruit ADS1x15](https://github.com/adafruit/Adafruit_ADS1X15) - Includes the drivers for [TI's ADS1115 chip](http://www.ti.com/product/ADS1115) which is built into the Mayfly board. (The ADS115 is a 16-bit analog-to-digital converter (ADC) with a programmable gain amplifier (PGA) and digital comparator.)
* [Sodaq DS3231](https://github.com/SodaqMoja/Sodaq_DS3231) - Controls the [DS3231](https://www.maximintegrated.com/en/products/digital/real-time-clocks/DS3231.html) Real Time Clock (RTC) built into the EnviroDIY Mayfly.
* [Sodaq RTCTimer](https://github.com/SodaqMoja/RTCTimer) - Works with the DS3231 to easily perform scheduled tasks.
* [EnviroDIY SoftwareSerialMod](https://github.com/EnviroDIY/SoftwareSerialMod) - A modification of the Arduino built-in SoftwareSerial library with ports corrected for working with other EnviroDIY Mayfly libraries

#### These libraries may be helpful, depending on which peripherals and sensors you have available and how you communicate with them.
* GPRSBee - Communicates with the [GPRSBee](https://www.seeedstudio.com/GPRSbee-rev.-6-p-2445.html#) to send data over cellular network.
* [EnviroDIY SDI-12](https://github.com/EnviroDIY/Arduino-SDI-12/tree/Mayfly) - Implements the [SDI-12](https://en.wikipedia.org/wiki/SDI-12) communications protocol that is used by a wide variety of environmental sensors.
* [Adafruit DHT](https://github.com/adafruit/DHT-sensor-library) - Controls the low cost [DHT](https://www.adafruit.com/products/385) temperature & humidity sensors sold by Adafruit.
* [Adafruit TSL2561](https://github.com/Adafruit/TSL2561-Arduino-Library/) - Controls the Adafruit [TSL2561](https://www.adafruit.com/products/439) digital luminosity sensor.
* [SDL SSD1306](https://github.com/switchdoclabs/SDL_Arduino_SSD1306)  - Controls the SwitchDoc Labs Grove [128x64 OLED](http://store.switchdoc.com/grove-128x64-i2c-oled-board-for-arduino-and-raspberry-pi/).

