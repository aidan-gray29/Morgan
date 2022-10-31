#! /usr/bin/python3

import sys
import aisentiment
import openai_hook

def getChatResponse(chatInput):
    aisentiment.getChatSentiment(chatInput)
    return openai_hook.getAIResponse(chatInput + "\n(Respond " + aisentiment.getSentimentString() + ")")

if __name__ == '__main__':
    openai_hook.init()

    print(getChatResponse(sys.argv[1]))

