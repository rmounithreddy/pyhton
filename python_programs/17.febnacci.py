#Print Fibonacci series up to n terms

n = int(input("Enter n: "))    #number of terms to be printed
def fibonacci(n):               #defining a functions
    a, b = 0, 1

    if n==1:    #in any case if user only want to print first term, this will handle that.
        print(a)
        return
    print(a)
    print(b)

    for i in range(2,n):  #since first two terms are already printed, loop will run from 2 to n-1
        c=a+b     #next term is the sum of previous two terms
        a=b           #for next iteration, we need to update a and b
        b=c           #here b is updated to c
        print(c)
fibonacci(n)     #calling the function