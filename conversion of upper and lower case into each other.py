# Write a program conversion of lower case letter to upper case letter and its vice versa:
ch=input("enter the letter that you want to find in the different case:")
if ch> 'A' and ch< 'Z':
    ch=ch.lower()
    print("the lower case letter is:",ch)
else:
    ch=ch.upper()
    print("the upper case letter is:",ch)