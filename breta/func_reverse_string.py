#take user input
#reverse the text
#print the reversed text as a string

def reverse_string(txt: str) -> str:
    text = list(txt)
    text.reverse()
    rtext = "".join(text)
    print(rtext)
    
reverse_string(input('Enter text here:'))