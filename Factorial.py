#to find the factorial of a natural number
x = int(input("Enter the number whose factorial is required: "))
fact = 1

if x < 0:
    print("Factorial doesn't exist for negative numbers. Please try again with a number greater than zero.")

elif x == 0:
    print("The required factorial: 1")

else:
    for i in range(1,x + 1):
        fact = fact*i
    print("The required factorial:",fact)





