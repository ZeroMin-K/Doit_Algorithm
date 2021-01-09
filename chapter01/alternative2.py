# print + and - alternately version 2

print('Print + and - alternately')
n = int(input('Count: '))

for _ in range(n //2):
    print('+-', end='')

if n % 2:
    print('+', end='')

print()