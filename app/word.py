import random
from requests import get
import os 
from dotenv import load_dotenv

load_dotenv()

def get_random_word():
    with open("./dictionary.txt", "r") as file:
        allText = file.read()
        words = list(map(str, allText.split()))
        word = random.choice(words)
        return word

def is_in_dictionary(status_code):
    return status_code == 200

def get_dictionary_entry(word):
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
        # sleep
        return get_dictionary_entry(word)
    response_body = response.json()
    return response_body
