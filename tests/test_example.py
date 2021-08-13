from app.example import *
from unittest.mock import patch
from tests.constants import *

def test_word_epiphany_doesnt_have_examples():   
    response_body = get_dictionary_entry("epiphany")
    examples = json_extract(response_body, 'text')
    assert examples == []

@patch('app.example.get_random_word')
def test_word_epiphany_doesnt_have_examples_get_another_word(get_random_word):
    result = get_word_example("epiphany")
    assert get_random_word.called is True

def word_cat_examples():
    response_body = get_dictionary_entry("cat")
    word_examples = json_extract(response_body, 'text')
    return word_examples

def test_word_cat_get_valid_examples():
    word_examples = word_cat_examples()
    assert word_examples[0] == 'a marbled cat'
    for word in word_examples:
        assert len(word.split()) != 1

@patch('app.example.get_random_word')
def test_word_cat_has_valid_examples(get_random_word):
    examples = get_word_example("cat")
    assert get_random_word.called is False

def test_example_is_too_short():
    result = is_example_valid(TEST_STR[0:1])
    assert not result

def test_example_is_too_long():
    result = is_example_valid(3*TEST_STR)
    assert not result

def test_example_is_valid():
    word_examples = word_cat_examples()
    for example in word_examples:
        if is_example_valid(example):
            example = lower_all_letters(example)
    assert example == 'the cat went crazy on the horn' or example == 'models fitted with a cat as standard'

def test_all_letters_are_lowered():
    result = lower_all_letters(TEST_STR)
    assert result == TEST_STR.lower()
