# sum of integer from a to b (for)

print('Calculate sum of integer from a to b')
a = int(input('Input integer a: '))
b = int(input('Input integer b: '))

if a > b:
    a, b = b, a     # sort a and b in ascending order

sum = 0
for i in range(a, b+1):
    sum += i

print(f'sum of integer from {a} to {b}: {sum}')