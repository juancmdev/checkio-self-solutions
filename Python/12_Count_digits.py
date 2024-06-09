'''
You need to count the number of digits in a given string.

Input: String.

Output: Integer.

Examples:
assert count_digits("hi") == 0
assert count_digits("who is 1st here") == 1
assert count_digits("my numbers is 2") == 1
assert (
    count_digits(
        "This picture is an oil on canvas painting by Danish artist Anna Petersen between 1845 and 1910 year"
    )
    == 8
)

'''
def count_digits(text: str) -> int:
    # your code here
    count = 0
    for i in text:
        if i.isdigit():
            count += 1
    return count

print(count_digits("5 plus 6 is 45"))