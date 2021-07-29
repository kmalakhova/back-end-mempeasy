# from example import get_word_example
# from word import word
from random import choice, randint


def build_password():
    symbols = ["~","!","@","#","$","*","(",")","_","-","+","=","?"]
    # sentence = get_word_example(word)
    sentence = "being a singer must be such a glamorous lifestyle!"
    content = sentence.split() # RESPLIT
    content = capitilize_random_word(content)
    if not any_symbols(content, symbols):
        content = add_symbol(content, symbols)
    if not any_number(content):
        content = add_number(content)
    print(content)
    # return content

    # split to set
    # capitalize random word
    # if char in char - cool
    #     not:
    #         pick randoom
    #         place random
    # if char is number - cool
    #     not:
    #         pick randoom
    #         place random

def capitilize_random_word(content):
    pick = ""
    while len(pick) < 3:
        pick = choice(content)
    return [word.upper() if word == pick else word for word in content]

def any_symbols(content,symbols):
    return any(word in symbols for word in content)

def add_symbol(content, symbols):
    symbol = choice(symbols)
    return [f"{word}{symbol}" if word == word.upper() else word for word in content]

def any_number(content):
    return any(word.isdigit() for word in content)

def add_number(content):
    num = randint(0, 10)
    N = len(content)
    placement = randint(0, N-1)
    return [f"{content[i]}{num}" if i == placement else content[i] for i in range(N)]




build_password()