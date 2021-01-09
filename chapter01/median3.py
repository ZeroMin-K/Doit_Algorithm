# input 3 integer and find median 1

def med3(a, b, c):
    # return median between a, b, c
    if a >= b:
        if b >= c:
            return b
        elif a <= c:
            return a
        else:
            return c
    elif a > c:
        return a
    elif b > c:
        return c
    else:
        return b

print('calculate median of 3 integers') 
a = int(input('Input value of integer a: '))
b = int(input('Input value of integer b: '))
c = int(input('input value of integer c: '))

print(f'median is {med3(a, b, c)}')