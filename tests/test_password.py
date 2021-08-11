from app.password import *
import pytest

pytest.test_str = "the pig likes to dig"
pytest.only_letters = ["the", "rat", "is", "fat"]
pytest.wsymbol = ["can", "you", "be", "ready", "at", "five", "?"]
pytest.wnumber = ["3",":","05","PM"]
pytest.wsymbol_wnumber = ["it", "is", "Aug", "10", "already", "!"]
pytest.symbols = ["!","$",":",";","?","-"]

def test_uppercase_random_word():
    sentence = uppercase_random_word(pytest.only_letters)
    assert any(word == word.upper() for word in sentence)

def test_sentence_has_symbol_returns_true():
    assert has_symbol(pytest.wsymbol, pytest.symbols)

def test_sentence_has_no_symbols_returns_false():
    assert not has_symbol(pytest.only_letters, pytest.symbols)

def test_add_symbol_to_sentence():
    sentence = uppercase_random_word(pytest.only_letters)
    sentence = add_symbol(sentence, pytest.symbols)
    assert has_symbol(sentence, pytest.symbols)

def test_sentence_has_number_returns_true():
    assert has_number(pytest.wnumber)

def test_sentence_has_no_numbers_returns_false():
    assert not has_number(pytest.wsymbol)

def test_add_random_number():
    sentence = add_number(pytest.only_letters)
    assert has_number(sentence)    

def test_get_first_letters():
    assert get_first_letters([pytest.wsymbol_wnumber[0].upper()] \
        + pytest.wsymbol_wnumber[1:]) == \
            ["IT", 'i','A','10','a','!']

def test_build_password():
    password, hint = build_password(hint = pytest.test_str)
    split_password = list(password)
    assert has_symbol(split_password, pytest.symbols)
    assert has_number(split_password)
    assert any(sym == sym.upper() for sym in split_password)
