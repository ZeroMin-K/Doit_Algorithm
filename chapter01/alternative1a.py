# print + and - alternately

print('Print + and - alternately')
n = int(input('Count: '))

for i in range(1, n +1):
    if i % 2:
        print('+', end='')
    else:
        print('-', end='')

print()