#count the number of digits in a number
num=int(input("Enter a number: "))
count=0
n=abs(num) #handeling negative numbers

while n>0:
    n=n//10
    count +=1
print(f"the number od digits in {num} id {count}")