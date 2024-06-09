'''
 In a given text you need to sum the numbers while excluding any digits that form part of a word.

The text consists of numbers, spaces and letters from the English alphabet.

example

Input: A string (str).

Output: An integer (int).

Examples:
assert sum_numbers("hi") == 0
assert sum_numbers("who is 1st here") == 0
assert sum_numbers("my numbers is 2") == 2
assert (
    sum_numbers(
        "This picture is an oil on canvas painting by Danish artist Anna Petersen between 1845 and 1910 year"
    )
    == 3755
)

'''

def sum_numbers(text: str) -> int:
    # your code here
    digit_list: list = []
    text = text.split()
    for x in text:
        if x.isdigit():
            x = int(x)
            digit_list.append(x)
    return sum(digit_list)

print(sum_numbers("my numbers is 2568 and 3569"))