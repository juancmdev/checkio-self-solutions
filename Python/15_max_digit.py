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
    value_list = [*value] #I get each value independently separated by semicolon, it's like doing a split
    result = int(max(value_list)) #I convert the result to an integer and obtain the maximum value
    return result

print(max_digit(65345))