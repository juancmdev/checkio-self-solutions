'''
You should return a given string in reverse order.

example

Input: A string (str).

Output: A string (str).

Examples:
assert backward_string("val") == "lav"
assert backward_string("") == ""
assert backward_string("ohho") == "ohho"
assert backward_string("123456789") == "987654321"

'''

def backward_string(val: str) -> str:
    # your code here
    my_list = []
    for i in val:
        my_list.insert(0, i) # insert() --> Adds an element at the specified position
    return ("".join(my_list))

print(backward_string("Hello World"))