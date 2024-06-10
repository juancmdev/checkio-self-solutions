'''
Not all of the elements are important. What you need to do here is to remove from the sequence all of the elements before the given one.

example

For the illustration we have a sequence [1, 2, 3, 4, 5] and we need to remove all elements that go before 3 - which are 1 and 2.

We have two edge cases here: (1) if a cutting element cannot be found, then the sequence shoudn't be changed. (2) if the sequence is empty, then it should remain empty.

Input: List and the border element.

Output: List or another Iterable (tuple, iterator, generator).

Examples:
assert list(remove_all_before([1, 2, 3, 4, 5], 3)) == [3, 4, 5]
assert list(remove_all_before([1, 1, 2, 2, 3, 3], 2)) == [2, 2, 3, 3]
assert list(remove_all_before([1, 1, 2, 4, 2, 3, 4], 2)) == [2, 4, 2, 3, 4]
assert list(remove_all_before([1, 1, 5, 6, 7], 2)) == [1, 1, 5, 6, 7]

'''

#from collections.abc import Iterable


def remove_all_before(items: list, border: int): #-> Iterable:
    # your code here
    if items.count(border) > 0: #Guaranted border exist in list
        find_index = items.index(border) #find index border
        return items[find_index:] #return all numbers from find-index to the finish of the list
    else:
        return items

print(remove_all_before([1, 2, 3, 4, 5], 3))