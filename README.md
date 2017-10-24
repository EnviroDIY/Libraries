# Libraries
This repository contains _**links**_ to various libraries that are used to support functions and features of the EnvidoDIY Mayfly Data Logger board.  Please note that these libraries are not maintained in this repository, but rather are independent repositories that are linked as submodules of this repository.

Please let us know if you have any trouble installing the libraries!

### Installing Libraries in the [Arduino.cc IDE](https://www.arduino.cc/en/Main/Software):

The simplest way to use these libraries is to right-click on this carefully crafted **[-->->link<-<--](https://github.com/EnviroDIY/Libraries/blob/master/libraries.zip?raw=true)**, select "save link as", and save the file somewhere on your computer.  You can also click on "libraries.zip" in the file list above and then click the grey download button on that page to download the zip.  In your the Arduino Software (IDE), import that zip file following the instructions for _"Manual Installation"_ from https://www.arduino.cc/en/Guide/Libraries#toc5.  You _cannot_ directly import the zip using the Arduino Library Manager because it contains multiple libraries.

To update the libraries, you will need to re-download the zip file and overwrite the folders in your Arduino libraries folder.

Please _**DO NOT**_ to use the green "Clone or Download" button to try to download a zip file.  The zip downloaded that way will only contain empty folders instead of the libraries themselves.

If you prefer, and are familiar with Git, clone this repo into your Arduino\libraries folder.  The libraries should then be accessible to the Arduino Software (IDE).  Each library can also be downloaded individually by clicking on that library and then downloading a ZIP of only that library.

### Installing Libraries in [PlatformIO](http://platformio.org/):

The library manager in PlatformIO is far superior to anything in the [Arduino.cc IDE](https://www.arduino.cc/en/Main/Software).  I highly recommend using PlatformIO if you intend to do anything beyond very simple programming.

To install the entire collection on PlatformIO enter this command into the terminal:

`pio lib -g install https://github.com/EnviroDIY/Libraries.git#platformio`

To update all libraries, run the command:

`pio lib -g update`

## Included Libraries

#### These libraries are for basic components built into the EnviroDIYMayfly:
* [Adafruit ADS1x15](https://github.com/adafruit/Adafruit_ADS1X15) - Includes the drivers for the auxillary ADC [TI's ADS1115 chip](http://www.ti.com/product/ADS1115) which is built into the Mayfly board. (The ADS115 is a 16-bit analog-to-digital converter (ADC) with a programmable gain amplifier (PGA) and digital comparator.)
* [Sodaq DS3231](https://github.com/SodaqMoja/Sodaq_DS3231) - Controls the [DS3231](https://www.maximintegrated.com/en/products/digital/real-time-clocks/DS3231.html) I2C Real Time Clock (RTC) built into the EnviroDIY Mayfly.


#### These libraries are likely to be helpful when using the Mayfly as a sleeping logger:
* [EnviroDIY Modular Sensors](https://github.com/EnviroDIY/ModularSensors) - A class-subclass setup allowing many sensors to be called with the same commands.  This library is dependent on many of the other libraries listed here.
* [Sodaq RTCTimer](https://github.com/SodaqMoja/RTCTimer) - Works with the DS3231 to easily perform scheduled tasks.
* [SdFat](https://github.com/greiman/SdFat) - Communicates with the onboard SD card to read and save data on the card.  This is a more efficient and more feature rich replacement of the built-in SD library.
* [EnableInterrupt](https://github.com/EnviroDIY/EnableInterrupt) - Administrates and handles pin change interrupts on the Atmel microcontroller built into the Mayfly.  This allows to Mayfly to sleep and save battery.  This library also works well as a controller for the versions of SoftwareSerial and SDI-12 linked below that have been stripped of interrupt control.
* [Sodaq PCInt](https://github.com/SodaqMoja/Sodaq_PcInt) - Another library that can administrate pin change interrupts.  _Note that in order to use this library simultaneously with SoftwareSerial or the SDI-12 library you must instead use the PcIntMod referenced above._
* [EnviroDIY_GPRSbee](https://github.com/EnviroDIY/GPRSbeeMod/tree/v1.2_hacked) - Communicates with the [Sodaq GPRSBee](https://www.seeedstudio.com/GPRSbee-rev.-6-p-2445.html#) to send data over cellular network.  This library is an older version of the Sodaq library that has been hacked to work with both rev0.4 and rev0.6 of the GPRSbee.  Further work is required to make the current Sodaq GPRSbee library work on the EnviroDIY Mayfly.
* [Tiny GSM](https://github.com/EnviroDIY/TinyGSM.git) - A smaller GSM communication library that supports, among others, [Sodaq's GPRSBee](https://shop.sodaq.com/en/gprsbee.html), Digi's [LTE](https://www.digi.com/products/xbee-rf-solutions/embedded-rf-modules-modems/digi-xbee-cellular) and [WiFi](https://www.digi.com/products/xbee-rf-solutions/embedded-rf-modules-modems/xbee-wi-fi) XBees, and ESP8266 based WiFi-XBee's like [Itead's Wee](https://www.itead.cc/wiki/Wee_Serial_WIFI_Module) or [DFRobot's Wifi Bee](https://www.dfrobot.com/product-1279.html).  This library is more compact (and possibly easier to use) than the [EnviroDIY_GPRSbee](https://github.com/EnviroDIY/GPRSbeeMod/tree/v1.2_hacked) and supports many more modules, but does not include direct support for putting the modems to sleep.  The "ModemSupport" module of the [EnviroDIY Modular Sensors](https://github.com/EnviroDIY/ModularSensors) library does adds that.


#### These libraries are used communicate with sensors and peripherals:
* [EnviroDIY SDI-12](https://github.com/EnviroDIY/Arduino-SDI-12) - Implements the [SDI-12](https://en.wikipedia.org/wiki/SDI-12) communications protocol that is used by a wide variety of environmental sensors.  _Note that in order to use this library simultaneously with SoftwareSerial or the Sodaq PcInt library you must instead use the SDI-12Mod referenced below._
* [SensorModbusMaster](https://github.com/EnviroDIY/SensorModbusMaster) - Implements the [Modbus RTU](https://en.wikipedia.org/wiki/Modbus) communications protocol that is used by a wide variety of industrial sensors.
* [Adafruit Sensor](https://github.com/adafruit/Adafruit_Sensor) - Adafruit unified sensor library/driver used by many of Adafruit's other sensor libraries.
* [Adafruit DHT](https://github.com/adafruit/DHT-sensor-library) - Controls the low cost [AOSong DHT11, DHT21, AM2301, DHT22, or AM2302](http://www.aosong.com/en/products/index.asp) temperature & humidity sensors sold by [Adafruit](https://www.adafruit.com/products/385) and others.
* [Adafruit TSL2561](https://github.com/Adafruit/TSL2561-Arduino-Library/) - Controls the Adafruit [TSL2561](https://www.adafruit.com/products/439) digital luminosity sensor.
* [Adafruit AM2315](https://github.com/adafruit/Adafruit_AM2315) - Controls and communicates with an [AOSong AM2315](www.aosong.com/asp_bin/Products/en/AM2315.pdf) encased I2C temperature and humidity sensor
* [Adafruit BME280 Library](https://github.com/adafruit/Adafruit_BME280_Library) - Controls and communicates with a [Bosch BME280](https://www.bosch-sensortec.com/bst/products/all_products/bme280) humidity, barometric pressure and temperature sensor.
* [OneWire](https://github.com/PaulStoffregen/OneWire) - Lets you access 1-wire devices made by Maxim/Dallas, such as temperature sensors and ibutton secure memory. For temperature sensors, the DallasTemperature library can be used with this library.
* [Dallas Temperature](https://github.com/milesburton/Arduino-Temperature-Control-Library) - Arduino plug and go library for the Maxim (previously Dallas) DS18B20 (and similar) temperature ICs
* [YosemitechModbus](https://github.com/EnviroDIY/YosemitechModbus) - Communicates with [Yosemitech](http://www.yosemitech.com/en/) brand modbus sensors.
* [SDL SSD1306](https://github.com/switchdoclabs/SDL_Arduino_SSD1306)  - Controls the SwitchDoc Labs Grove [128x64 OLED](http://store.switchdoc.com/grove-128x64-i2c-oled-board-for-arduino-and-raspberry-pi/).



#### These libraries are modified versions that are necessary in order to work together:

These modified versions are necessary because each of these libraries will try to simultaneously monitor all pin change interrupt vectors on any Arduino board causing compiler errors.  Instead of allowing them to handle interrupts on their own, these have been stripped of interrupt vector control and require and external pin change interrupt to set up their interrupts for them.  The modified versions are only necessary to use two or more of these together.  Any pin that supports pin change interrupts can be used with these libraries, provided that you use [EnableInterrupt](https://github.com/EnviroDIY/EnableInterrupt) or another library to allow them interrupt control.  These can also be used with other AVR boards (including the Arduino Uno, Mega, or Leonardo).
* [EnviroDIY SoftwaterSerial_ExtInts](https://github.com/EnviroDIY/SoftwaterSerial_ExternalInts)
* [EnviroDIY SDI-12_ExtInts](https://github.com/EnviroDIY/Arduino-SDI-12/tree/ExtInts)

Instead of being controlled by an alternate library, these versions have been cropped to only look at only one interrupt vector each. This means they are each only able to operate on the specified pins rather than any pin that supports pin change interrupts.  These will only work together with the listed pin numbers on the EnviroDIY Mayfly itself.
* [EnviroDIY PCInt_PCINT0](https://github.com/EnviroDIY/PcIntMod) - Will only work on pins D24-D31 (A00-A07)
* [EnviroDIY SoftwareSerial_PCINT12](https://github.com/EnviroDIY/SoftwareSerialMod) - Will only work on pins D8-D23
* [EnviroDIY SDI-12_PCINT3](https://github.com/EnviroDIY/Arduino-SDI-12/tree/Mayfly) - Will only work on pins D0-D7
