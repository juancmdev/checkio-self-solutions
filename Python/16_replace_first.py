'''
 In a given sequence the first element should become the last one. An empty sequence or with only one element should stay the same.

example

Input: List.

Output: List or another Iterable (tuple, iterator, generator).

Examples:
assert replace_first([1, 2, 3, 4]) == [2, 3, 4, 1]
assert replace_first([1]) == [1]
assert replace_first([]) == []

'''

def replace_first(items: list) -> list:
    # your code here
    if len(items) > 1:
        to_delete = items[0] #item to be deleted
        items.remove(items[0]) #remove item in position 0
        items.append(to_delete) #append removed item to de finish
    return items

print(replace_first([1, 2, 3, 4]))