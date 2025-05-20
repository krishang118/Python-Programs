#solving 1 + x + x^2.. x^n for x and n

x = int(input("Enter the number whose series is required, that is x: "))
n = int(input("Enter the number of terms which are required, that is n: "))
sum = 0
for i in range(0,n):
    sum += x**i
print("The required sum of the series is",sum)



