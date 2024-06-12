'''
 Split the string into pairs of two characters. If the string contains an odd number of characters, then the missing second character of the final pair should be replaced with an underscore ('_').

Input: A string.

Output: A list or another Iterable of strings.

Example:
assert list(split_pairs("abcd")) == ["ab", "cd"]
assert list(split_pairs("abc")) == ["ab", "c_"]
assert list(split_pairs("abcdf")) == ["ab", "cd", "f_"]
assert list(split_pairs("a")) == ["a_"]

'''
from typing import Iterable


def split_pairs(text: str) -> Iterable[str]:
    # your code here
    length = len(text)
    n = 0
    my_list = []

    if length % 2:
        pass
    else:
        x = text[0:n + 2]
        my_list.append(x)
        print(my_list)
    return text

print(split_pairs("abcd"))