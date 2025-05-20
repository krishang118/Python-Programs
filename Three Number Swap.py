#accepting 3 nos. and 1st becomes 2nd, 2nd becomes 3rd, 3rd becomes 1st
a=int(input("Enter 1st number: "))
b=int(input("Enter 2nd number: "))
c=int(input("Enter 3rd number: "))
print("nos. before swapping: ", a,b,c)
a,b,c = b,c,a
print("nos after swapping: ", a,b,c)
