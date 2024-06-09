'''
Try to find out how many zeros a given number has at the end.

example

Input: A non-negative integer (int).

Output: An integer (int).

Examples:
assert end_zeros(0) == 1
assert end_zeros(1) == 0
assert end_zeros(10) == 1
assert end_zeros(101) == 0

'''

def end_zeros(a: int) -> int:
    # your code here
    count = 0
    new_list = []
    a = str(a)
    a = [*a]
    for i in a:
        new_list.append(int(i))
        
    new_list.reverse()

    for j in new_list:
        if new_list[count] == 0:
            count += 1
    return count

print(end_zeros(1505))