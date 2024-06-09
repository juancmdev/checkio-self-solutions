'''
You are given a string and you have to find its first word.

The input string consists of only English letters and spaces.
There aren’t any spaces at the beginning and the end of the string.

example

Input: A string (str).

Output: A string (str). 


assert first_word("Hello world") == "Hello"
assert first_word("a word") == "a"
assert first_word("greeting from CheckiO Planet") == "greeting"
assert first_word("hi") == "hi"

How it is used: The first word is a command in a command line.

Precondition: The text can contain a-z, A-Z and spaces. 
'''

def first_word(text: str) -> str:
    # your code here
    return text.split()[0] #split(): Splits the string at the specified separator, and returns a list

print(first_word("Hello World"))