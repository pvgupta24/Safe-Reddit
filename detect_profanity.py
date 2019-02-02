from keras.preprocessing.text import text_to_word_sequence
from profanity_check import predict, predict_prob
import numpy as np

def tokenizeStrings(text):
    ans = text_to_word_sequence(text)
    return ans

def detectProfanity(words):
    # return a list of profane words, not a single word: 
    word_profanity = predict_prob(words)
    most_profane_words = []

    for i in range(0, len(word_profanity)):
        if word_profanity[i] > threshold:
            most_profane_words.append(i)


    return most_profane_words

def get_most_profane_words(text):
    words = tokenizeStrings(text)
    ans = detectProfanity(words)
    print("List of profane words:")
    for i in ans:
        print(i)

threshold = 0.5
get_most_profane_words('praveen sucks at all levels fucks')
