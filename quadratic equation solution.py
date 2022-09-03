# Write the program to find the roots of the quadratic equation:
a=float(input("enter the coefficient of X^2:"))
b=float(input("enter the coefficient of x:"))
c=float(input("enter the constant term:"))
d=b*b-4*a*c
print("the discriminator value is:",d)
if d>0:
    print("the roots are real and different")
    root1=(-b+d**.5)/(2*a)
    root2=(-b-d**.5)/(2*a)
    print("the roots are",root1,root2)
elif d==0:
    print("the roots are real and same")
    root1=root2=-b/(2*a)
else:
    print("the roots are imagenary and can be calculated with the help of iota")
