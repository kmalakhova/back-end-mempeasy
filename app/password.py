from app.example import get_word_example
from app.word import get_random_word
from random import choice, randint
import re

def uppercase_random_word(content): 
    """Converts random word(s) to uppercase"""
    pick = ""
    while len(pick) < 3 or not pick.isalpha():
        pick = choice(content)
    return [word.upper() if word == pick else word for word in content]

def has_symbol(content,symbols):
    """Checks if a sentence contains special symbols"""
    return any(word in symbols for word in content)

def add_symbol(content, symbols):
    """Adds random symbol after uppercase word(s)"""
    symbol = choice(symbols)
    l = []
    for word in content:
        l.extend([word, symbol]) if word == word.upper() and word.isalpha() else l.append(word)
    return l

def has_number(content):
    """Checks if a sentence contains a number"""
    return any(word.isdigit() for word in content)

def add_number(content):
    """Adds a random number to a random place in a sentence"""
    num = randint(0, 10)
    N = len(content)
    place = randint(0, N-1)
    l = []
    for i in range(N):
        l.extend([content[i], str(num)]) if i == place else l.append(content[i])
    return l

def get_first_letters(content):
    """Gets first characters of every word, except for the words in uppercase"""
    return [word if word == word.upper() else word[0] for word in content]

def build_password():
    """Builds secure password"""
    symbols = ["~","!","@","#","$","*","(",")","_","-","+","=","?",","]
    hint = (get_word_example(get_random_word()))
    content = re.findall(r"[\w']+|[.,!?;~@$*()+-=']", hint)
    content = uppercase_random_word(content)
    if not has_symbol(content, symbols):
        content = add_symbol(content, symbols)
    if not has_number(content):
        content = add_number(content)
    content = get_first_letters(content)
    password = "".join(content)
    return password, hint

def get_response():
    """Gets password and a hint"""
    password, hint = build_password()
    return password, hint
