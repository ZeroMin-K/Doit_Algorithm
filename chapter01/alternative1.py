# print + and - alternately version 1

print("Print + and - alternately")
n = int(input('Count: '))

for i in range(n):
    if i % 2:
        print('-', end = '')
    else:
        print('+', end='')

print()
    