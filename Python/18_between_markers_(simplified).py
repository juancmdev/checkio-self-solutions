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
    list_text = list(text)
    index_start = list_text.index(start)
    if text[index_start+1].isalpha():
        print(type(index_start))
        print(index_start)
        index_end = list_text.index(end)
        print(index_end)
        return list_text[index_start+1:index_end]
    else:
        return "vacío"
    

print(between_markers("What is ><", ">", "<"))