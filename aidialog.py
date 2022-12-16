#! /usr/bin/python3

import sys
import openai
import configparser

config = configparser.ConfigParser(interpolation=None)
file = 'confidential.ini'
section = 'OpenAI'
default = { 'api_key': '' }

def getResponse(chatInput):
    response = openai.Completion.create(
        model="text-ada-001",
        prompt=chatInput,
        max_tokens=30,
        temperature=0.6,
    )
    result=response.choices[0].text
    """ Output full response data for logging
    new = configparser.ConfigParser(interpolation=None)
    new['response'] = response
    with open('./ai-response.txt', 'w') as cf:
        new.write(cf)
    """
    return result

def authOpenAi():
    config.read(file)
    # If the section doesn't exist, append the default values to the file and exit
    if section not in config:
        config[section] = default
        with open(file, 'w') as configfile:
            config.write(configfile)

        raise ValueError(f"{section} tokens not found in {file} file. Please add them before running Morgan.")
    openai.api_key = config[section]['api_key']

if __name__ == '__main__':
    authOpenAi()
    print(getResponse(sys.argv[1]))

