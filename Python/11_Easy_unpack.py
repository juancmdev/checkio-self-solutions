'''
Your mission here is to create a function that gets a tuple and returns a tuple with only 3 elements - the first, third and second element from the last for the given tuple.

One important thing worth pointing out is that you need to use index in order to extract elements from the tuple. Pay attention, index counting starts from 0, not from 1. Which means that if you need to get the first element from the tuple elements, you should do elements[0], and the second element is elements[1].

example

Input: A tuple, at least 3 elements long.

Output: A tuple.

Examples:
assert easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)) == (1, 3, 7)
assert easy_unpack((1, 1, 1, 1)) == (1, 1, 1)
assert easy_unpack((6, 3, 7)) == (6, 7, 3)

'''

def easy_unpack(elements: tuple) -> tuple:
    # your code here
    x = elements[0]
    y = elements[2]
    z = elements[-2]
    return (x, y, z)

print(easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)))