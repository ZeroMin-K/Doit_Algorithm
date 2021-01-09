# sum of integers from 1 to n version 1 (while)

print('Calculate sum of integers from 1 to n')
n = int(input('Input n: '))

sum = 0
i = 1

while i <= n:
    sum += i
    i += 1

print(f'sum of integer from 1 to {n}: {sum}')
print(f'value of i: {i}')