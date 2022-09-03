# Write the program to make a simple calculator:
import math
print("..............CALCULATOR...............")
def add(a,b):
    return a+b
def sub(a,b):
    if a>b:
        return a-b
    else:
        return b-a
def mult(a,b):
    return a*b
def div(a,b):
    return a/b
def rem(a,b):
    return a%b
def sqr(a):
    return a*a
print("please enter your choice")
print("for add press 1")
print("for substract press 2")
print("for multiply press 3")
print("for divide press 4")
print("for remainder press 5")
print("for square of the no. press 6")


choice=int(input("enter the choice for Calculator"))
while(1):
    if choice==1:
        a=int(input("enter the first no."))
        b=int(input("enter the second no."))
        print("the summation the the above no. is",add(a,b))
    if choice==2:
        a=int(input(("enter the first no.")))
        b=int(input("enter the second no."))
        print("the difference is",sub(a,b))
    if choice ==3:
        a=int(input("enter the first no."))
        b=int(input("enter the second no."))
        print("the multiplication of the two no. is", mult(a,b))
    if choice == 4:
        a=int(input("enter the first no."))
        b=int(input("enter the second no."))
        print("the remainder of the given no. is",rem(a,b))
    if choice==5:
        a=int(input("enter the no."))
        print("the square of the given no. is",sqr(a))
    if choice>=6:
        print("Invalid selection")