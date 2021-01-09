# Calculate sum of integer from 1 to n (value of n is only positive)

print('Calculate sum of integer from 1 to n')

while True:
    n = int(input('Input n:'))
    if n > 0:
        break

sum = 0
i = 1

for i in range(1, n+1):
    sum += i
    i += 1

print(f'Sum of integer from 1 to {n}: {sum}')