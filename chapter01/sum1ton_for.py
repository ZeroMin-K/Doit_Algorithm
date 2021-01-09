# sum of integer from 1 to n version 2 (for)

print('Calculate sum of integers from 1 to n')
n = int(input('Input integer n:'))

sum = 0
for i in range(1, n+1):
    sum += i

print(f'sum of integers form 1 to {n}: {sum}')