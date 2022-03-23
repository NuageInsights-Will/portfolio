#take user input
#reverse the text
#print the reversed text as a string

def string_rev(txt: str) -> str:
    text = txt[::-1]
    print(text)
    return text

print(string_rev("hello"))