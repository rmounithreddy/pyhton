num=int(input("Enter a number: "))
if num<0:
    print("Factorial does not exist for negative numbers")
elif num==0:
    print("the factorioal of 0 is 1")
else:
    factorial=1
    for i in range(1,num+1):
        factorial=factorial*i
    print("the factorial of ",num, "is ",factorial)