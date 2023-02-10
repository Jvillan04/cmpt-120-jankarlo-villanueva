#ascii_lowercase is basically a built in dictiontary where a=1 and so on...
from string import ascii_lowercase as alphabet


# Defining the join_strings function with the parameter strings

def join_strings(strings):
    return "".join(strings)
# Note To Self: The qoutes in "".join(strings) just allow the the list from test_functions.py to be added into the function.


def mad_libs(name, noun, event):
    return f"{name} is too cool for {noun} class. Instead she/he will be attending the {event}"




def caesar_cipher(text, shift):
    result = ""
    charlook = {char: alphabet[(i + shift) % 26] for i, char in enumerate(alphabet)}
    for i in text.lower():
        result += charlook.get(i, i)
    return result