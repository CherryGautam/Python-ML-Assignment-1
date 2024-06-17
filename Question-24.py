print("Enter the operators (+, -, *, /) for the desired operation")
x=float(input("Enter the first number: "))
y=float(input("Enter the second number: "))
c=input("Enter the operator of choice: ")

if c=="+" :
    print(x,"+",y,"=",x+y)
elif c=="-":
    print(x,"-",y,"=",x-y)
elif c=="*":
    print(x,"*",y,"=",x*y)
elif c=="/":
    if y==0:
        print("Division by zero is undefined")
    else:
        print(x,"/",y,"=",x/y)
else:
    print("Invalid operator")
