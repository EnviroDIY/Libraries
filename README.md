# Libraries
This repository contains _**links**_ to various libraries that are used to support functions and features of the EnvidoDIY Mayfly Data Logger board.  Please note that these libraries are not maintained in this repository, but rather are independent repositories that are linked as submodules of this repository.

Please let us know if you have any trouble installing the libraries!

### Installing Libraries in the [Arduino.cc IDE](https://www.arduino.cc/en/Main/Software):

The simplest way to use these libraries is to right-click on the file "libraries.zip", select "save link as", and save the file somewhere on your computer.  In your the Arduino Software (IDE), import that zip file following the instructions for "Manual Installation" from https://www.arduino.cc/en/Guide/Libraries.  To update the libraries, you will need to re-download the zip file and overwrite the folders.

Please _**DO NOT**_ to use the green "Clone or Download" button to try to download a zip file.  The zip downloaded that way will only contain empty folders instead of the libraries themselves.

If you prefer and are familiar with Git, clone this repo into your Arduino\libraries folder.  The libraries should then be accessible to the Arduino Software (IDE).  Each library can also be downloaded individually by clicking on that library and then downloading a ZIP of only that library.

### Installing Libraries in [PlatformIO](http://platformio.org/):

To install the entire collection on PlatformIO enter this command into the terminal:
`pio lib -g install https://github.com/EnviroDIY/Libraries.git#platformio.`
To update all libraries, run the command:
`pio lib -g update.`

#### These libraries are for basic components built into the EnviroDIYMayfly:
* [Adafruit ADS1x15](https://github.com/adafruit/Adafruit_ADS1X15) - Includes the drivers for the auxillary ADC [TI's ADS1115 chip](http://www.ti.com/product/ADS1115) which is built into the Mayfly board. (The ADS115 is a 16-bit analog-to-digital converter (ADC) with a programmable gain amplifier (PGA) and digital comparator.)
* [Sodaq DS3231](https://github.com/SodaqMoja/Sodaq_DS3231) - Controls the [DS3231](https://www.maximintegrated.com/en/products/digital/real-time-clocks/DS3231.html) Real Time Clock (RTC) built into the EnviroDIY Mayfly.


#### These libraries are likely to be helpful when using the Mayfly as a sleeping logger
* [EnviroDIY Modular Sensors](https://github.com/EnviroDIY/ModularSensors) - A class-subclass setup allowing many sensors to be called with the same commands.  This library is dependent on many of the other libraries listed here.
* [Sodaq RTCTimer](https://github.com/SodaqMoja/RTCTimer) - Works with the DS3231 to easily perform scheduled tasks.
* [Sodaq PCInt](https://github.com/SodaqMoja/Sodaq_PcInt) - Administrates and handles pin change interrupts on the Atmel microcontroller built into the Mayfly.  This allows to Mayfly to sleep and save battery.  _Note that in order to use this library simultaneously with SoftwareSerial or the SDI-12 library you must instead use the PcIntMod referenced below._
* [EnviroDIY SDI-12](https://github.com/EnviroDIY/Arduino-SDI-12) - Implements the [SDI-12](https://en.wikipedia.org/wiki/SDI-12) communications protocol that is used by a wide variety of environmental sensors.  _Note that in order to use this library simultaneously with SoftwareSerial or the Sodaq PcInt library you must instead use the SDI-12Mod referenced below._
* [SdFat](https://github.com/greiman/SdFat) - Communicates with the onboard SD card to read and save data on the card.  This is a more efficient and more feature rich replacement of the built-in SD library.
* [EnviroDIY_GPRSbee](https://github.com/EnviroDIY/GPRSbeeMod/tree/v1.2_hacked) - Communicates with the [GPRSBee](https://www.seeedstudio.com/GPRSbee-rev.-6-p-2445.html#) to send data over cellular network.  This library is an older version of the Sodaq library that has been hacked to work with both rev0.4 and rev0.6 of the GPRSbee.  Further work is required to make the current Sodaq GPRSbee library work on the EnviroDIY Mayfly.


#### These libraries used in the workshop and Mayfly tutorials
* [Adafruit Sensor](https://github.com/adafruit/Adafruit_Sensor) - Adafruit unified sensor library.
* [Adafruit DHT](https://github.com/adafruit/DHT-sensor-library) - Controls the low cost [DHT](https://www.adafruit.com/products/385) temperature & humidity sensors sold by Adafruit.
* [Adafruit TSL2561](https://github.com/Adafruit/TSL2561-Arduino-Library/) - Controls the Adafruit [TSL2561](https://www.adafruit.com/products/439) digital luminosity sensor.
* [SDL SSD1306](https://github.com/switchdoclabs/SDL_Arduino_SSD1306)  - Controls the SwitchDoc Labs Grove [128x64 OLED](http://store.switchdoc.com/grove-128x64-i2c-oled-board-for-arduino-and-raspberry-pi/).


#### These libraries are modified versions that are necessary in order to work together on the EnviroDIY Mayfly

The modified versions are necessary because each of these 3 libraries will try to simultaneously monitor all 4 pin change interrupt vectors on the Mayfly causing conflicts.  They have been cropped to only look at one each.  The modified versions are only necessary to use two or more of these together.
* [EnviroDIY PCInt_PCINT0](https://github.com/EnviroDIY/PcIntMod)
* [EnviroDIY SoftwareSerial_PCINT12](https://github.com/EnviroDIY/SoftwareSerialMod)
* [EnviroDIY SDI-12_PCINT3](https://github.com/EnviroDIY/Arduino-SDI-12/tree/Mayfly)
