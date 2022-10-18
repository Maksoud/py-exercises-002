# This function checks if a word is a palindome or not

def palindrome(text):
    txt = text.replace(' ','')
    return txt == txt[::-1]

result1 = palindrome('nurses run')
print(result1) # True