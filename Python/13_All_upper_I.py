'''
 Check if a given string has all symbols in upper case. If the string is empty 
 or doesn't have any letter in it - function should return True.

example

Input: A string (str).

Output: A logic value (bool).

Examples:
assert is_all_upper("ALL UPPER") == True
assert is_all_upper("all lower") == False
assert is_all_upper("mixed UPPER and lower") == False
assert is_all_upper("") == True
1
2
3
4

Precondition: a-z, A-Z, 1-9 and spaces 
'''

def is_all_upper(text: str) -> bool:
    # your code here
    return text.upper() == text

print(is_all_upper("Juan"))