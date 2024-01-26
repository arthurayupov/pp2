#Example
#1.
x = 1    # int
y = 2.8  # float
z = 1j   # complex
#2.
print(type(x))
print(type(y))
print(type(z))
#3.
x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))
#4.
x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))
#5.
x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))
#6.
x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))
#7.
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#Convert from int to float:
a = float(x)

#Convert from float to int:
b = int(y)

#Convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))
#8.
import random

print(random.randrange(1, 10))

#exercise:
#1.
x = 5
x = float
(x)
#2. 
x = 5.5
x = int(x)
#3.
x = 5
x = complex(x)