#swap two numbers without using third variable
a = 5
b = 10 
print("Before swapping: a =", a, "b =", b)
a, b = b, a
print("After swapping: a =", a, "b =", b)
#swap two numbers using third variable
x = 15
y = 20
print("Before swapping: x =", x, "y =", y)
temp = x
x = y
y = temp
print("After swapping: x =", x, "y =", y)