from app.word import get_dictionary_entry, get_random_word
from app.extract import json_extract

def is_example_valid(example):
    """Validates that a sentence is of a suitable length"""
    return len(example.split()) < 10 and len(example.split()) > 3

def lower_all_letters(example):
    "Lowers all letters in a sentence"
    return example.lower()

def get_word_example(word):
    """Retrieves sentences with a given word from a response body"""
    response_body = get_dictionary_entry(word)
    word_examples = set(json_extract(response_body, 'text'))
    for example in word_examples:
        if is_example_valid(example):
            example = lower_all_letters(example)
            return example
    return get_word_example(get_random_word())

