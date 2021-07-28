from word import *
from requests import get
import os # what is os?
from dotenv import load_dotenv

load_dotenv()

def is_in_dictionary(status_code): # Do I even need this piece?
    return status_code == 200
# @ move to word
def search_word(word): #? lookupword? get_dictionary_entry
    # word = search?
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
        return search_word(word)
    response_body = response.json()
    return response_body

# print(search_word(get_random_word()))