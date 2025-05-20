name = 'superb'

for ch in name:
    print(ch,'-',end = ' ')


string1 = input("Enter a string: ")
print(string1, "in reverse order is:")
length = len(string1)
for a in range(-1,(-length -1), -1):
    print(string1[a])


n= int(input("Enter a no.: "))
s=str(n)
if '0' in s:
    print("There's a 0 in",s)
else:
    print("There isn't a 0 in",s)


print('='*30)
print('\n'*9)
print('='*30)


string = '#'
pattern = ' '
for a in range(5):
    pattern += string
    print(pattern)


