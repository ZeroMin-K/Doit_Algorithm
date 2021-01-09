# Print * n times and begin a new line when it is w times

print('Print *')
n = int(input('Count to print: '))
w = int(input('Count for new line: '))

for i in range(n):
    print('*', end='')
    if i % w == w-1:
        print()

if n % w:
    print()