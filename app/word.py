import random
from requests import get
import os 
from dotenv import load_dotenv

load_dotenv()

def get_random_word():
    """Fetches random word from txt file"""
    with open("./dictionary.txt", "r") as file:
        allText = file.read()
        words = list(map(str, allText.split()))
        word = random.choice(words)
        return word

def is_in_dictionary(status_code):
    """Checks if a word is in Oxford Dictionary"""
    return status_code == 200

def get_dictionary_entry(word):
    """Sends GET request to Oxford Dictionary"""
    APP_KEY = os.environ.get("APP_KEY")
    APP_ID = os.environ.get("APP_ID")
    API_BASE_URL = "https://od-api.oxforddictionaries.com"
    language = 'en-us'
    fields = 'examples'
    strictMatch = 'false'
    url = API_BASE_URL + ':443/api/v2/entries/' + language + '/' + word + '?fields=' + fields + '&strictMatch=' + strictMatch;

    response = get(url, headers = {'APP_ID': APP_ID, 'APP_KEY': APP_KEY})

    status_code = response.status_code
    if not is_in_dictionary(status_code):
        word = get_random_word() 
        # sleep() or not to sleep(), that is the question
        return get_dictionary_entry(word)
    response_body = response.json()
    return response_body
