# input positive two digits

print('Input positive two digits')

while True:
    no = int(input('Input value: '))
    if no >= 10 and no <= 99:           # equal 10 <= no 99
        break

print(f'Input postivie integers is {no}')
