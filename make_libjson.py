##############################################################################
# This creates a JSON file to be read by PlatformIO to group these libraries.
# Created By: Sara Damiano (sdamiano@stroudcenter.org)
# Created On: 2/15/2017
##############################################################################

import json

library = {"name": "EnviroDIYMayfly",
           "description": ('A collection of libraries to support the ' +
                           'EnviroDIY Mayfly'),
           "keywords": ('Mayfly, EnviroDIY, sensors, DS-3231, logger, ' +
                        'SDI-12, libraries'),
           "repository": {"type": "git", "url":
                          "https://github.com/EnviroDIY/Libraries.git",
                          "branch": "platformio"},
           "export": {"exclude": ["*/.gitattributes", "*/.gitignore",
                                  "*/.travis.yml", "*/.gitmodules",
                                  "*id_rsa.enc", "*/platformio.ini", "*/*.sh",
                                  "*/make-zip.sh", "*/Doxyfile",
                                  "*/.git/*", "*/.github/*"]
                      }
           }

dependencies = []
dep = {}
with open('.gitmodules', 'r') as submods:
    for num, line in enumerate(submods, 1):

        if line.split()[0] == "path":
            dep['name'] = line.split()[2]

        if line.split()[0] == "url":
            url = line.split()[2]
            if not url.endswith(".git"):
                url += ".git"
            dep['version'] = url
        if line.split()[0] == "branch" and line.split()[2] != "master":
            url += "#" + line.split()[2]
            dep['version'] = url

        # Fix up dependencies that are part of the PlatformIO index
        if 'name' in dep and 'version' in dep:
            if dep['name'] == 'Adafruit_ADS1X15':
                dep['name'] = 'Adafruit ADS1X15'
                dep['note'] = ('TI ADS1X15 ADC Library by Adafruit')
                dep['library id'] = '342'
                dep['url'] = dep.pop('version')
                dep['authors'] = ["Adafruit"]
            if dep['name'] == 'Adafruit_AM2315':
                dep['name'] = 'Adafruit AM2315'
                dep['note'] = ('AOSong AM2315 I2C Temp/Humidity ' +
                               'Sensor Library by Adafruit')
                dep['library id'] = '773'
                dep['url'] = dep.pop('version')
                dep['authors'] = ["Adafruit"]
            if dep['name'] == 'Adafruit_BME280':
                dep['name'] = 'Adafruit BME280 Library'
                dep['note'] = ('Bosch BME280 Temp/Humidity/Pressure ' +
                               'Sensor Library by Adafruit')
                dep['library id'] = '166'
                dep['url'] = dep.pop('version')
                dep['authors'] = ["Adafruit"]
            if dep['name'] == 'Adafruit_DHT':
                dep['name'] = 'DHT sensor library'
                dep['note'] = ('AOSong DHT Sensor Library by Adafruit')
                dep['library id'] = '19'
                dep['url'] = dep.pop('version')
                dep['authors'] = ["Adafruit"]
            if dep['name'] == 'Adafruit_Sensor':
                dep['name'] = 'Adafruit Unified Sensor'
                dep['note'] = ('Adafruit Unified Sensor Library')
                dep['library id'] = '31'
                dep['url'] = dep.pop('version')
                dep['authors'] = ["Adafruit"]
            if dep['name'] == 'Adafruit_TSL2561':
                dep['name'] = 'Adafruit TSL2561'
                dep['note'] = ('TAOS TSL2561 Luminosity Sensor Library ' +
                               'by Adafruit')
                dep['library id'] = '34'
                dep['url'] = dep.pop('version')
                dep['authors'] = ["Adafruit"]
            if dep['name'] == 'DallasTemperature':
                dep['note'] = ('DallasTemperature - Arduino Library for ' +
                               'Dallas Temperature ICs (DS18B20, DS18S20, ' +
                               'DS1822, DS1820)')
                dep['library id'] = '54'
                dep['url'] = dep.pop('version')
                dep['authors'] = ["Guil Barros", "Miles Burton",
                                  "Rob Tillart", "Tim Nuewsome"]
            if dep['name'] == 'EnableInterrupt':
                dep['note'] = ('GreyGnome\'s EnableInterrupt - Assign an ' +
                               'interrupt to any supported pin on all ' +
                               'Arduinos')
                dep['library id'] = '311'
                dep['url'] = dep.pop('version')
                dep['authors'] = ["Mike 'GreyGnome' Schwager"]
            if dep['name'] == 'EnviroDIY_DS3231':
                dep['note'] = ('An Arduino library for the DS3231 RTC ' +
                               '(Real Time Clock), based off of the ' +
                               'Sodaq_DS3231 library.')
                dep['library id'] = '2079'
                dep['url'] = dep.pop('version')
                dep['authors'] = ["Kees Bakker", "Sara Damiano"]
            if dep['name'] == 'EnviroDIY_GPRSBee':
                dep['name'] = 'GPRSbee'
                dep['note'] = ('An Arduino library for the SODAQ GPRSbee.')
                dep['authors'] = ["Kees Bakker"]
            if dep['name'] == 'EnviroDIY_ModularSensors':
                dep['note'] = ('EnviroDIY ModularSensors - A library that ' +
                               'allows access to multiple sensors through a ' +
                               'unified interface.')
                dep['library id'] = '1648'
                dep['url'] = dep.pop('version')
                dep['authors'] = ["Sara Damiano", "Shannon Hicks"]
            if dep['name'] == 'EnviroDIY_PCInt_PCINT0':
                dep['name'] = 'Sodaq_PcInt_PCINT0'
                dep['note'] = ('Sodaq library controlling pin change ' +
                               'interrupts - modified to use only interrupt ' +
                               'vector 0.')
                dep['authors'] = ["Kees Bakker"]
            if dep['name'] == 'EnviroDIY_SDI12':
                dep['name'] = 'Arduino-SDI-12'
                dep['note'] = ('EnviroDIY SDI-12 Library')
                dep['library id'] = '1486'
                dep['url'] = dep.pop('version')
                dep['authors'] = ["Kevin M. Smith",
                                  "Sara Damiano", "Shannon Hicks"]
            if dep['name'] == 'EnviroDIY_SDI12_ExtInts':
                dep['name'] = 'Arduino-SDI-12_ExtInts'
                dep['note'] = ('EnviroDIY SDI-12 Library - modified to use ' +
                               'interrupts called by an external library.')
                dep['authors'] = ["Kevin M. Smith",
                                  "Sara Damiano", "Shannon Hicks"]
            if dep['name'] == 'EnviroDIY_SDI12_PCINT3':
                dep['name'] = 'Arduino-SDI-12_PCINT3'
                dep['note'] = ('EnviroDIY SDI-12 Library - modified to use ' +
                               'only interrupt vector 3.')
                dep['authors'] = ["Kevin M. Smith",
                                  "Sara Damiano", "Shannon Hicks"]
            if dep['name'] == 'EnviroDIY_SoftwareSerial_ExtInts':
                dep['name'] = 'SoftwareSerial_ExtInts'
                dep['note'] = ('Arduino SoftwareSerial  Library - modified ' +
                               'to use interrupts called by an external ' +
                               'library.')
            if dep['name'] == 'EnviroDIY_SoftwareSerial_PCINT12':
                dep['name'] = 'SoftwareSerial_PCINT12'
                dep['note'] = ('Arduino SoftwareSerial  Library - modified ' +
                               'to use only interrupt vectors 1 and 2.')
            if dep['name'] == 'OneWire':
                dep['note'] = ('OneWire - Control 1-Wire protocol ' +
                               '(DS18S20, DS18B20, DS2408 and etc)')
                dep['library id'] = '1'
                dep['url'] = dep.pop('version')
                dep['authors'] = ["Paul Stoffregen", "Tom Pollard",
                                  "Derek Yerger", "Jim Studt", "Jason Dangel",
                                  "Robin James", "Ken Butcher",
                                  "Guillermo Lovato", "Scott Roberts",
                                  "Bertrik Sikken", "Mark Tillotson",
                                  "Glenn Trewitt", "Josh Larios"]
            if dep['name'] == 'RTCZero':
                dep['note'] = ('Functions for using the processor real time ' +
                               'clock in SAMD21 processors')
                dep['library id'] = '873'
                dep['url'] = dep.pop('version')
                dep['authors'] = ["Arduino"]
            if dep['name'] == 'SdFat':
                dep['note'] = ('SdFat - FAT16/FAT32 file system for SD cards.')
                dep['library id'] = '322'
                dep['url'] = dep.pop('version')
                dep['authors'] = ["Bill Greiman"]
            if dep['name'] == 'SDL_SSD1306':
                dep['note'] = ('Library for SwitchDoc Labs Grove OLED 128x64')
                dep['authors'] = ["SwitchDoc Labs"]
            if dep['name'] == 'SensorModbusMaster':
                dep['note'] = ('EnviroDIY SensorModbusMaster - Arduino ' +
                               'library for communicating via modbus with ' +
                               'the Arduino acting as the modbus master.')
                dep['library id'] = '1824'
                dep['url'] = dep.pop('version')
                dep['authors'] = ["Sara Damiano"]
            if dep['name'] == 'Sodaq_PcInt':
                dep['note'] = ('Sodaq Pin Change Interrupt Library')
                dep['library id'] = '695'
                dep['authors'] = ["Kees Bakker"]
                dep['url'] = dep.pop('version')
            if dep['name'] == 'Sodaq_RTCTimer':
                dep['name'] = 'RTCTimer'
                dep['note'] = ('Sodaq Real Time Clock (RTC) Timer Library ')
                dep['library id'] = '645'
                dep['url'] = dep.pop('version')
                dep['authors'] = ["Kees Bakker"]
            if dep['name'] == 'TinyGSM':
                dep['note'] = ('A small Arduino library for GPRS modules.')
                dep['authors'] = ["Volodymyr Shymanskyy"]
            if dep['name'] == 'YosemitechModbus':
                dep['note'] = ('Arduino library for communication with ' +
                               'Yosemitech sensors via Modbus.')
                dep['library id'] = '2078'
                dep['url'] = dep.pop('version')
                dep['authors'] = ["Sara Damiano"]

        if (line.split()[0] == "[submodule") and num != 1:
            dependencies.append(dep)
            dep = {}
    else:
        dependencies.append(dep)
submods.close()

library['dependencies'] = dependencies

jsonfile = open('library.json', 'w')
json.dump(library, jsonfile, indent=4, separators=(',', ': '))
jsonfile.close()
