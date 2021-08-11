from app.password import *
import pytest
symbols = ["!","$",":",";","?","-"]


class Vars():
    test_str = "the pig likes to dig"
    only_letters = ["the", "rat", "is", "fat"]
    wsymbol = ["can", "you", "be", "ready", "at", "five", "?"]
    wnumber = ["3",":","05","PM"]
    wsymbol_wnumber = ["it", "is", "Aug", "10", "already", "!"]

def test_uppercase_random_word():
    sentence = uppercase_random_word(Vars.only_letters)
    assert any(word == word.upper() for word in sentence)

def test_sentence_has_symbol_returns_true():
    assert has_symbol(Vars.wsymbol,symbols)

def test_sentence_has_no_symbols_returns_false():
    assert not has_symbol(Vars.only_letters,symbols)

def test_add_symbol_to_sentence():
    sentence = uppercase_random_word(Vars.only_letters)
    sentence = add_symbol(sentence, symbols)
    assert has_symbol(sentence,symbols)

def test_sentence_has_number_returns_true():
    assert has_number(Vars.wnumber)

def test_sentence_has_no_numbers_returns_false():
    assert not has_number(Vars.wsymbol)

def test_add_random_number():
    sentence = add_number(Vars.only_letters)
    assert has_number(sentence)    

def test_get_first_letters():
    assert get_first_letters([Vars.wsymbol_wnumber[0].upper()] \
        + Vars.wsymbol_wnumber[1:]) == \
            ["IT", 'i','A','10','a','!']

def test_build_password():
    password, hint = build_password(hint = Vars.test_str)
    split_password = list(password)
    assert has_symbol(split_password, symbols)
    assert has_number(split_password)
    assert any(sym == sym.upper() for sym in split_password)
