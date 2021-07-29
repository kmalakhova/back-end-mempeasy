from word import get_dictionary_entry
from word import get_random_word
from extract import json_extract

def get_word_example(word):
    response_body = get_dictionary_entry(word)
    word_examples = json_extract(response_body, 'text')
    for example in word_examples:
        if is_example_valid(example):
            return example
    return get_word_example(get_random_word())

def is_example_valid(example):
    return len(example.split()) < 10 and len(example.split()) > 5

print(get_word_example(get_random_word()))