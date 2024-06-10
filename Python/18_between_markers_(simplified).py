'''
 You are given a string and two markers (the initial one and final). You have to find a substring enclosed between these two markers. But there are a few important conditions.

    The initial and final markers are always different.
    The initial and final markers are always 1 char size.
    The initial and final markers always exist in a string and go one after another.

example

Input: Three arguments. All of them are strings (str). The second and third arguments are the initial and final markers.

Output: A string (str).

Examples:
assert between_markers("What is >apple<", ">", "<") == "apple"
assert between_markers("What is [apple]", "[", "]") == "apple"
assert between_markers("What is ><", ">", "<") == ""
assert between_markers("[an apple]", "[", "]") == "an apple"

'''

def between_markers(text: str, start: str, end: str) -> str:
    # your code here
    list_text = list(text) # convert the list to text
    index_start = list_text.index(start) # Find index where program have to start 
    if text[index_start+1].isalpha(): # If the next character after te start is alpha
        index_end = list_text.index(end) # Find index where program have to end
        res = list_text[index_start+1:index_end] #I crop from and to what the program should display
        final_res = "".join([str(el) for el in res])
        return final_res
    else:
        return""

print(between_markers("[an apple]", "[", "]"))