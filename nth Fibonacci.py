#computing the nth number/member of the fibonacci series

n= int(input("Enter the numbering at which number is required(from the fibonacci series): "))
if n<0:
    print("The number can't be computed for numbering zero. Please enter a value greater than 0.")

x = 1
y = 1
z = 0
i = 3


while i<=n:
    z = x+y
    x = y
    y = z
    i = i+1

print("The required number:",z)


