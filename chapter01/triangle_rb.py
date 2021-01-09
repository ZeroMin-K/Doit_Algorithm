# print * shaped isoceles traingle which right bottom is right angle

print('print * shaped isoceles traingle which right bottom is right angle')

n = int(input('Input lenght of shorter side: '))
for i in range(n):
    for _ in range(n-i-1):
        print(' ', end='')
    for _ in range(i+1):
        print('*', end='')
    print()