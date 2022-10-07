import configparser

# Used as the basis for the twitter.py config changes.
# This can be modified as needed for other files.
config = configparser.ConfigParser(interpolation=None)
file = 'confidential.ini'

# Initialize blank values
# ONLY add them in the unshared .ini file
default = {'bearer_token': '',
           'consumer_key': '',
           'consumer_secret': '',
           'access_token': '',
           'access_token_secret': ''}

config.read(file)
if 'Twitter' not in config:
    config['Twitter'] = default
    with open(file, 'w') as configfile:
        config.write(configfile)
    
    raise ValueError("Twitter tokens not found in %s file. Please add them before running Morgan." % file)

for key, value in config['Twitter'].items():
    print(key, ':', value)

