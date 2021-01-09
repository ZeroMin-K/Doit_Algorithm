# print * shaped isoceles traingle which left bottom is right angle

print('print * shaped isoceles traingle which left bottom is right angle')
n = int(input('Input lenght of shorter side: '))

for i in range(n):
    for j in range(i + 1):
        print('*', end='')
    print()