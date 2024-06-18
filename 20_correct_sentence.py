'''
Correct Sentence

For the input of your function, you will be given one sentence. You have to return a corrected version, that starts with a capital letter and ends with a period (dot).
Pay attention to the fact that not all of the fixes are necessary. If a sentence already ends with a period (dot), then adding another one will be a mistake.

example

Input: A string (str).

Output: A string (str).

Examples:
assert correct_sentence("greetings, friends") == "Greetings, friends."
assert correct_sentence("Greetings, friends") == "Greetings, friends."
assert correct_sentence("Greetings, friends.") == "Greetings, friends."
assert correct_sentence("greetings, friends.") == "Greetings, friends."
1
2
3
4

Precondition: No leading and trailing spaces, text contains only spaces, a-z, A-Z, "," and ".". 

'''

def correct_sentence(text: str) -> str:
    # your code here
    my_list = []
    x = text.split()
    return x

print(correct_sentence("greetings, friends"))