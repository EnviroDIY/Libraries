##############################################################################
# This creates a JSON file to be read by PlatformIO to group these libraries.
# Created By: Sara Damiano (sdamiano@stroudcenter.org)
# Created On: 2/15/2017
##############################################################################

import json

library = {"name": "EnviroDIYMayfly",
           "description": "A collection of libraries to support the EnviroDIY Mayfly",
           "keywords": "Mayfly, EnviroDIY, Sensors, DS-3231",
           "repository": {"type": "git", "url": "https://github.com/EnviroDIY/Libraries.git", "branch": "master"}
           }

dependencies = []
with open('.gitmodules','r') as submods:
    for num, line in enumerate(submods, 1):
        if line.split()[0] == "path":
            dep = {'name': line.split()[2]}
        if line.split()[0] == "url":
            url = line.split()[2] + ".git"
            dep['version'] = url
        if line.split()[0] == "branch":
            url += "#" + line.split()[2]
            dep['version'] = url
        if (line.split()[0] == "[submodule") and num != 1:
            dependencies.append(dep)
    else:
        dependencies.append(dep)
submods.close()

library['dependencies'] = dependencies

jsonfile = open('libraries.json', 'w')
json.dump(library, jsonfile, indent=1, separators=(',', ': '))
jsonfile.close()

