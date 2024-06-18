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
    dot = '.'
    length = len(text) #find the length of the text

    if text[length - 1] == dot: #Ask if the text contains a dot
        text_split = text.split() #Split the text and save it in a list
        text_split[0] = text_split[0].capitalize() #Capitalize first character
        new_text = " ".join(text_split) # I convert a list to a text string
        return new_text
    
    else:
        text_split = text.split() #Split the text and save it in a list
        text_split[0] = text_split[0].capitalize() #Capitalize first character
        new_text = " ".join(text_split) #I convert a list to a text string
        new_text += '.' # Add a dot to the finish of the string
        return new_text
        


print(correct_sentence("greetings, friends"))