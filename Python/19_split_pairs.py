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