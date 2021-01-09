# enumerate length of side of rectangle with integer width, height and area

area = int(input('Input area of rectangle: '))

for i in range(1, area +1):
    if i * i > area:
        break
    if area % i:
        continue
    print(f'{i} x {area // i}')