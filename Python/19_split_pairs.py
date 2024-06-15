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
    if len(text) % 2:
        text = text + "_"
        return text

    
    result: list = []
    while text:
        result.append(text[:2])
        text = text[2:]
        return result

print(split_pairs("abcdrf"))