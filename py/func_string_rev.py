#take user input
#reverse the text
#print the reversed text as a string

def string_rev(txt: str) -> str:
    text = txt[::-1]
    print(text)
    
string_rev(input('Enter text here:'))