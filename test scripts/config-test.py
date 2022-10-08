# Used as the basis for the twitter.py config changes.
# This can be modified as needed for other files.

import configparser

# Disable interpolation so strings can be parsed literally
# Important for non-alphanumeric characters
config = configparser.ConfigParser(interpolation=None)
file = 'confidential.ini'

# Section to read from the config, should be changed to Twitter, Discord, etc
section = 'Test'

# Initialize blank values for the needed keys
# ONLY add values in the unshared .ini file
default = {
    'key1': '',
    'key2': '',
    'key3': ''
}

config.read(file)

# If the section doesn't exist, append the default values to the file and exit
if section not in config:
    config[section] = default
    with open(file, 'w') as configfile:
        config.write(configfile)
    
    raise ValueError(f"{section} tokens not found in {file} file. Please add them before running Morgan.")

# Will print the existing INI values
for key, value in config[section].items():
    print(key, ':', value)
