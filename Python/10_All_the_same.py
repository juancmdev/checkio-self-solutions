'''
 In this mission you should check if all elements in the given sequence are equal.

example

Input: List.

Output: Logic value (bool).

Examples:
assert all_the_same([1, 1, 1]) == True
assert all_the_same([1, 2, 1]) == False
assert all_the_same([1, "a", 1]) == False
assert all_the_same([1, 1, 1, 2]) == False

'''

from typing import List, Any


def all_the_same(elements: List[Any]) -> bool:
    # your code here
    count = 1
    length = len(elements)
    
    if count <= length - 1:
        for i in range(0, length):
            if count == length:
                break
            if elements[count] == elements[i]:
                count += 1
            else:
                return False
    return True

print(all_the_same([2,2,2,9]))