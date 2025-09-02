def addition (x,y):
    return x+y

def subract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    return x/y

print("select operation.")
print("1.add")
print("2.subtract")
print("3.mutiply")
print("4.divide")

op='y'
while(op=='y'):
    #take input from the user.
    choice=input ("enter choice(1/2/3/4):")


    num1=int(input("enter first number:"))
    num2=int(input("enter second number:"))

if choice=='1':
    print(num1,"+",num2,"=",add(num1,num2))
elif choice=='2':
    print(num1,"-",num2,"=",subtract(num1,num2))
elif choice=='3':
    print(num1,"*",num2,"=",multiply(num1,num2))
elif choice=='4':
    print(num1,"/",num2,"=",divide(num1,num2))


else:
    print("invalid input")

op=input("do you want to continue(y/n):")
