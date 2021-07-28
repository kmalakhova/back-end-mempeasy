# from routes import search_word
import random
import requests

def get_random_word(): # save loc
    res = requests.get("https://raw.githubusercontent.com/dolph/dictionary/master/popular.txt")
    # words = list(map(str, res.content.split()))
    words = [word.decode() for word in res.content.split()]
    word = random.choice(words)
    # print(type(word))
    # print(word)
    return word
    # return "cat"

# get_random_word()