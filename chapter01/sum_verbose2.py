# sum of integer from a to b version 2

print('Calculate sum of integer from a to b')
a = int(input('Input integer a: '))
b = int(input('Input integer b: '))

if a > b:
    a, b = b, a

sum = 0
for i in range(a, b):
    print(f'{i} + ', end = ' ')
    sum += i

print(f'{b} = ', end = '')
sum += b
print(sum)