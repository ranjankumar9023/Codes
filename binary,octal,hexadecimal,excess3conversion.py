# Write a program to find the binary, octal, hexadecimal and excess 3 with decimal no.
x=int(input("enter the no. that you want to find the different conversion:"))
print("the binary of ",x ," is:",bin(x))
print("the octal of ",x ,"is:",oct(x))
print("the hexadecial of ",x,"is:",hex(x))
print("the excess 3 of",x,"is:",bin(x+3))