# sum of integer from a to b version 1

print('calculate sum of integer from a to b')
a = int(input('Input integer a:'))
b = int(input('Input integer b:'))

if a > b:
    a, b = b, a

sum = 0
for i in range(a, b+1):
    if i < b:      
        print(f'{i} + ', end = ' ')
    else:
        print(f'{i} = ', end = ' ')
    sum += i

print(sum)