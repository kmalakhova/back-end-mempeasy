from routes import search_word
from word import get_random_word
from extract import json_extract

def get_word_example(word):
    response_body = search_word(word)
    word_examples = json_extract(response_body, 'text') # Find every instance of `text`
    for example in word_examples:
        if is_example_valid(example):
            return example
    return get_word_example(get_random_word())

def is_example_valid(example):
    return len(example.split()) < 10 and len(example.split()) > 5
print(get_word_example(get_random_word()))