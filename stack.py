l=[]
while(1):
    choice=print('''
    1. push in the list:-
    2. Pop from the list:-
    3. peek from the list:-
    4. Display the list:-
    5. Exit''')

    if choice==1: # Pushing the data into the stack
        n=input("enter the value that you want to push")
        a=l.append(n)
        print(a)
    elif choice==2:
        if len(l)==0:
            print("Empty stack")
        else:
            b=print("the last element:" ,l[-1])
            l=l.remove(b)
            print("new stack",l)
    elif choice==3:
        if len(l)==0:
            print("Empty stack")
        else:
            print("the peek element is:",l[-1])

    elif choice==4:
        print("the stack is:",l)
    elif choice==5:
        break


