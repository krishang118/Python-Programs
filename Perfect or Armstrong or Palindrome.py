#to determine if a number is a perfect no.,an armstrong no. or a palindrome number

x = int(input("Enter a positive number: "))
if(x==0)or(x<0):
    print("Enter only a positive number please.")

sd = 0
for i in range(1,x):
    if(x%i == 0):
        sd += i

num = x
z = x
i = 0
r = 0
c = 0
while num > 0:
    num = num//10
    i = i + 1
for c in range(0,i):
    r = r*10 + z%10
    z = z//10
print("The number you entered, in reverse order is",r)

sc = 0
temp = x
while temp > 0:
    digit = temp % 10
    sc += digit**3
    temp //= 10
if(x==sc):
    print("The number is an armstrong number.")
elif(x==r):
    print("The number is a palindrome number.")
elif(x==sd):
    print("The number is a perfect number.")
else:
    print("The number isn't armstrong, neither prime nor a perfect number.")
