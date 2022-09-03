# Write the program to find the factorial of the a number:
def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
x=int(input("enter the no. that you want for factorial="))
print("the result is",fact(x))