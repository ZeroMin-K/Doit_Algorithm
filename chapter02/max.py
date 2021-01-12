from typing import Any, Sequence

def max_of(a: Sequence) -> Any:
    # return maximum element of Sequence a

    maximum = a[0]
    for i in range(1, len(a)):
        if a[i] > maximum:
            maximum = a[i]
    return maximum

if __name__ == '__main__':
    num = int(input('Input integer: '))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'Input value of x[{i}]: '))
    
    print(f'maximum is {max_of(x)}')