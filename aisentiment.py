#! /usr/bin/python3

import openai_hook

sentiment_score = 0
total_posts = 1 # Used for initial sentiment weights

def addSentimentScore(sentiment):
    global sentiment_score
    global total_posts
    
    score = 0 # Neutral
    sentiment = sentiment.lower()

    if "negative" in sentiment or "hate" in sentiment:
        score = -1
    elif "positive" in sentiment or "love" in sentiment:
        score = 1
    
    # Add in the new score, weighted against the average of the previous scores
    sentiment_score *= total_posts
    total_posts += 1
    sentiment_score += score
    sentiment_score /= total_posts

def getSentimentString():
    global sentiment_score

    if sentiment_score < -0.6:
        return "hate"
    if sentiment_score < -0.2:
        return "sad"
    if sentiment_score > 0.2:
        return "happy"
    if sentiment_score > 0.6:
        return "love"
    return "neutral"

def getChatSentiment(chatInput):
    global sentiment_score

    sentiment = openai_hook.getAIResponse("Sentence: " + chatInput + "\nSentiment: (rate positive, neutral, or negative)")
    sentiment = sentiment.strip().split(' ')[0]

    # Occasionally GPT-3 can't parse a sentiment, assume neutral
    if not sentiment:
        sentiment = "Neutral"
    
    print(f"Sentiment: {sentiment}")
    addSentimentScore(sentiment)
    print(f"Current score: {sentiment_score}")
    return sentiment