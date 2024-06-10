'''
You have a string that consist only of digits. You need to find how many zero digits ("0") are at the beginning of the given string.

example

Input: A string (str), that consists of digits.

Output: An integer (int).

Examples:
assert beginning_zeros("100") == 0
assert beginning_zeros("001") == 2
assert beginning_zeros("100100") == 0
assert beginning_zeros("001001") == 2

'''

def beginning_zeros(a: str) -> int:
    # your code here
    count = 0
    list_a = [*a] #I get each value independently separated by semicolon, it's like doing a split
    for num in list_a:
        num = int(num) #Convert str num to int
        if num == 0:
            count += 1 # Add 1 to count
        else:
            break #If num is diferent to 0 finish the loop

    return count

print(beginning_zeros('001001'))