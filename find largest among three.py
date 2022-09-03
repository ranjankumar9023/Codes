# Write a program to find the greatest no. among the three numbers:
x=int(input("enter the first no.:"))
y=int(input("enter the second no.:"))
z=int(input("enter the third no.:"))

if x>y:
    if x>z:
        print("the largest no. is:",x)
    else:
        print("the largest no. is:",z)
else:
    print("the largest no. is:",y)
