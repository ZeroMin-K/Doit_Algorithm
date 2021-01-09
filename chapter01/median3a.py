# input 3 integer and find median 2

def med3(a, b, c):
    # return median of a, b, c
    if (b >= a and c <= a) or (b <= a and c >= a):
        return a
    elif (a > b and c < b) or (a < b and c > b):
        return b
    return c

print('calculate median of 3 integers') 
a = int(input('Input value of integer a: '))
b = int(input('Input value of integer b: '))
c = int(input('input value of integer c: '))

print(f'median is {med3(a, b, c)}')