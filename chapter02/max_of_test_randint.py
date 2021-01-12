import random
from max import max_of

print('Calculate maximum of random number')
num = int(input('Input number of random number: '))
lo = int(input('Input minium of random number: '))
hi = int(input('Input maximum of random number: '))
x = [None] * num
for i in range(num):
    x[i] = random.randint(lo, hi)

print(f'{x}')
print(f'maximum: {max_of(x)}')