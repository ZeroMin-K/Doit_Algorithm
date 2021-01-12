from max import max_of

print('Calculate maximum of array')
print('Caution: exit wehen input "Exnd"')

number = 0
x = []

while True:
    s = input(f'Input value of x[{number}]: ')
    if s == 'End':
        break
    x.append(int(s))
    number += 1

print(f'You input {number} integers')
print(f'Maximum is {max_of(x)}')