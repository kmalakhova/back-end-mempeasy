from example import get_word_example
from word import get_random_word
from random import choice, randint
import re

def has_capital_letter(content):
    return any(word[0] == word[0].upper() for word in content)

def capitilize_random_word(content): 
    pick = ""
    while len(pick) < 2 or pick.isdigit():
        pick = choice(content)
    return [word.upper() if word == pick else word for word in content]

def has_symbol(content,symbols):
    return any(word in symbols for word in content)

def add_symbol(content, symbols):
    symbol = choice(symbols)
    l = []
    for word in content:
        l.extend([word, symbol]) if word == word.upper() else l.append(word)
    return l

def has_number(content):
    return any(word.isdigit() for word in content)

def add_number(content):
    num = randint(0, 10)
    N = len(content)
    place = randint(0, N-1)
    l = []
    for i in range(N):
        l.extend([content[i], str(num)]) if i == place else l.append(content[i])
    return l

def get_first_letters(content):
    return [word if word[0] == word[0].upper() else word[0] for word in content]

def get_hint():
    hint = (get_word_example(get_random_word()))
    # print(hint)
    return hint

def build_password():
    symbols = ["~","!","@","#","$","*","(",")","_","-","+","=","?"]
    # sentence = get_hint()
    sentence = "I fear he may have muddled the message"
    content = re.findall(r"[\w']+|[.,!?;~@$*()+-=']", sentence)
    if not has_capital_letter(content):
        content = capitilize_random_word(content)
    # print(f"The result of capitilize_random_word\n{content}")
    if not has_symbol(content, symbols):
        content = add_symbol(content, symbols)
    # print(f"The result of add_symbol\n{content}")
    if not has_number(content):
        content = add_number(content)
    # print(f"The result of add_number\n{content}")
    content = get_first_letters(content)
    # print(f"The result of get_first_letters\n{content}")
    return content

def get_password():
    content = build_password()
    password = "".join(content)
    # print(password)
    return password

print((get_password()))