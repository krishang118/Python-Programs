#inputting a string and determining whether it is a palindrome or not..
#...and also converting case of characters in a string.

string = input("Enter a string: ")
if string == string[::-1]:
    print("The entered string is a palindrome.")
else:
    print("The entered string is not a palindrome.")

print("The string after the conversion:",string.swapcase())


