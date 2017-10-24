##############################################################################
# This creates a JSON file to be read by PlatformIO to group these libraries.
# Created By: Sara Damiano (sdamiano@stroudcenter.org)
# Created On: 2/15/2017
##############################################################################

import json

library = {"name": "EnviroDIYMayfly",
           "description": "A collection of libraries to support the EnviroDIY Mayfly",
           "keywords": "Mayfly, EnviroDIY, Sensors, DS-3231, Logger, SDI-12",
           "repository": {"type": "git", "url": "https://github.com/EnviroDIY/Libraries.git", "branch": "platformio"},
           "export": {"exclude": ["*/.gitattributes", "*/.gitignore", "*/.travis.yml",
                                  "*/.gitmodules", "*id_rsa.enc", "*/platformio.ini",
                                  "*/*.sh", "*/make-zip.sh", "*/Doxyfile", "*/.git/*",
                                  "*/.github/*"]
                     }
           }

dependencies = []
dep = {}
with open('.gitmodules','r') as submods:
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
                dep['note'] = 'TI ADS1X15 ADC Library by Adafruit'
                dep['name'] = '342'
                dep['url'] = dep.pop('version')
            if dep['name'] == 'Adafruit_DHT':
                dep['note'] = 'AOSong DHT Sensor Library by Adafruit'
                dep['name'] = '19'
                dep['url'] = dep.pop('version')
            if dep['name'] == 'Adafruit_Sensor':
                dep['note'] = 'Adafruit Unified Sensor Library'
                dep['name'] = '31'
                dep['url'] = dep.pop('version')
            if dep['name'] == 'Adafruit_TSL2561':
                dep['note'] = 'TAOS TSL2561 Luminosity Sensor Library by Adafruit'
                dep['name'] = '34'
                dep['url'] = dep.pop('version')
            if dep['name'] == 'Adafruit_AM2315':
                dep['note'] = 'AOSong AM2315 I2C Temp/Humidity Sensor Library by Adafruit'
                dep['name'] = '166'
                dep['url'] = dep.pop('version')
            if dep['name'] == 'Adafruit_BME280':
                dep['note'] = 'Bosch BME280 Temp/Humidity/Pressure Sensor Library by Adafruit'
                dep['name'] = '773'
                dep['url'] = dep.pop('version')
            if dep['name'] == 'EnviroDIY_SDI12':
                dep['note'] = 'EnviroDIY SDI-12 Library'
                dep['name'] = '1486'
                dep['url'] = dep.pop('version')
            if dep['name'] == 'Sodaq_PcInt':
                dep['note'] = 'Sodaq Pin Change Interrupt Library'
                dep['name'] = '695'
                dep['url'] = dep.pop('version')
            if dep['name'] == 'Sodaq_RTCTimer':
                dep['note'] = 'Sodaq Real Time Clock (RTC) Timer Library '
                dep['name'] = '645'
                dep['url'] = dep.pop('version')
            if dep['name'] == 'SdFat':
                dep['note'] = 'SdFat'
                dep['name'] = '322'
                dep['url'] = dep.pop('version')
            if dep['name'] == 'OneWire':
                dep['note'] = 'OneWire'
                dep['name'] = '1'
                dep['url'] = dep.pop('version')
            if dep['name'] == 'DallasTemperature':
                dep['note'] = 'DallasTemperature'
                dep['name'] = '54'
                dep['url'] = dep.pop('version')
            if dep['name'] == 'RTCZero':
                dep['note'] = 'RTCZero'
                dep['name'] = '873'
                dep['url'] = dep.pop('version')
            if dep['name'] == 'SensorModbusMaster':
                dep['note'] = 'EnviroDIY SensorModbusMaster'
                dep['name'] = '1824'
                dep['url'] = dep.pop('version')
            if dep['name'] == 'EnableInterrupt':
                dep['note'] = 'GreyGnome\'s EnableInterrupt'
                dep['name'] = '311'
                dep['url'] = dep.pop('version')

        if (line.split()[0] == "[submodule") and num != 1:
            print num
            print dep
            dependencies.append(dep)
            dep = {}
submods.close()

library['dependencies'] = dependencies

jsonfile = open('library.json', 'w')
json.dump(library, jsonfile, indent=1, separators=(',', ': '))
jsonfile.close()
