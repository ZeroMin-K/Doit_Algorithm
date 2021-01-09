# generate n random number between 10 and 99 (stop when 13 is generated)

import random
n = int(input('Input number of random number: '))

for _ in range(n):
    r = random.randint(10, 99)
    print(r, end=' ')
    if r == 13:
        print('\nStop Program')
        break
else:
    print('\nStop generating random number')