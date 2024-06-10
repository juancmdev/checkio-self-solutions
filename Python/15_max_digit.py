'''
 You have a number and you need to determine which digit in this number is the biggest.

example

Input: A positive integer (int).

Output: An integer 0-9 (int).

Examples:
assert max_digit(0) == 0
assert max_digit(52) == 5
assert max_digit(634) == 6
assert max_digit(1) == 1

'''

def max_digit(value: int) -> int:
    # your code here
    value = str(value)
    value = [*value]
    return value

print(max_digit(6534589))