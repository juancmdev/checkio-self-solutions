'''
You have a non-negative integer. Try to find out how many digits it has.

example

Input: A non-negative integer (int).

Output: An integer (int).

Examples:
assert number_length(10) == 2
assert number_length(0) == 1
assert number_length(4) == 1
assert number_length(44) == 2

'''
def number_length(value: int) -> int:
    x = "".join(str(value)) # join() --> Converts the elements of an iterable into a string
    return int(len(x))

print(number_length(3652))