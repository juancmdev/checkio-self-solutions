'''
 Check if the given number is even or not. Your function should return True if the number is even, and False if the number is odd.

Input: An integer (int).

Output: Logic value (bool).

Examples:
assert is_even(2) == True
assert is_even(5) == False
assert is_even(0) == True

'''

def is_even(num: int) -> bool:
    # your code here
    if num % 2 == 0:
        return True
    else:
        return False
    
print(is_even(16))