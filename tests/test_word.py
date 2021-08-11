from app.word import *

def test_get_random_word_from_dictionary():
    word = get_random_word()
    assert word != ""

def test_get_dictionary_entry_for_word_cat():
    response = get_dictionary_entry("cat")
    assert response != []
    assert len(response) == 4

def test_word_is_not_in_oxford_dictionary_get_another_word():
    response = get_dictionary_entry("invalidword")
    assert response != []
