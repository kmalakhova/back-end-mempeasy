from app.password import *
from tests.constants import *

def test_uppercase_random_word():
    sentence = uppercase_random_word(ONLY_LETTERS)
    assert any(word == word.upper() for word in sentence)

def test_sentence_has_symbol_returns_true():
    assert has_symbol(WSYMBOL, SYMBOL)

def test_sentence_has_no_SYMBOL_returns_false():
    assert not has_symbol(ONLY_LETTERS, SYMBOL)

def test_add_symbol_to_sentence():
    sentence = uppercase_random_word(ONLY_LETTERS)
    sentence = add_symbol(sentence, SYMBOL)
    assert has_symbol(sentence, SYMBOL)

def test_sentence_has_number_returns_true():
    assert has_number(WNUMBER)

def test_sentence_has_no_numbers_returns_false():
    assert not has_number(WSYMBOL)

def test_add_random_number():
    sentence = add_number(ONLY_LETTERS)
    assert has_number(sentence)    

def test_get_first_letters():
    assert get_first_letters([WSYMBOL_WNUMBER[0].upper()] \
        + WSYMBOL_WNUMBER[1:]) == \
            ["IT", 'i','A','10','a','!']

def test_build_password():
    password, hint = build_password(hint = TEST_STR)
    split_password = list(password)
    assert has_symbol(split_password, SYMBOL)
    assert has_number(split_password)
    assert any(sym == sym.upper() for sym in split_password)
