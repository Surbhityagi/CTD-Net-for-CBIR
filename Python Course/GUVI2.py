# MODULE 2 of GUVI
# Variables

#Type conversion
a = int(10)
b = 13
b = float(b)
print(a)
print(b)

# will return the type of variable
print(type(b))

# Way of declaring multiple variables.
x,y,z= 12, 24,35
print(x)
print(y)
print(z)

a=b=c= "I LOVE MY INDIA"
print(a)
print(b)
print(c)
print(a[3])
print(b[4])

#Length function
print(len(c))

#Slice function
print(a[2:6])
print(a.lower())

#Replace function
print(b.replace("I", "E"))

# Split function
print(b.split("-"))

# Conditional Statements

a = 16
b = 16
if a > b:
    print("a is greater")
elif a == b:
    print("both are equal")
else:
    print("b is greater")

# Function

def firstFunction():
    print("This is the first function")

firstFunction()

def nextFun(x):
    print(x + " " + "This is the 2nd One")

nextFun("Hii!!!")