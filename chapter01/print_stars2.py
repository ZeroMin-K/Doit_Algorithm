# print * n times and begin a new line when it is w times version 2

print('Print *')
n = int(input('Count to print: '))
w = int(input('Count for new line: '))

for _ in range(n // w):
    print('*' * w)

rest = n % w
if rest:
    print('*' * rest)