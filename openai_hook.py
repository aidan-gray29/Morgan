#! /usr/bin/python3

import sys
import openai
import configparser

config = configparser.ConfigParser(interpolation=None)
file = 'confidential.ini'
section = 'OpenAI'
default = { 'api_key': '' }

def init():
    config.read(file)

    # If the section doesn't exist, append the default values to the file and exit
    if section not in config:
        config[section] = default
        with open(file, 'w') as configfile:
            config.write(configfile)

        raise ValueError(f"{section} tokens not found in {file} file. Please add them before running Morgan.")

    openai.api_key = config[section]['api_key']

def getAIResponse(chatInput):
    response = openai.Completion.create(
        model="text-ada-001",
        prompt=chatInput,
        max_tokens=50,
        temperature=0.6,
        top_p=1.0,
        frequency_penalty=0.5,
        presence_penalty=0.0
    )
    result=response.choices[0].text
    return result

if __name__ == '__main__':
    print(getAIResponse(sys.argv[1]))

