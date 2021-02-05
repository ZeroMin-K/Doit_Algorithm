# 비재귀적인 퀵 정렬 구현

from stack import Stack
from typing import MutableSequence

def qsort(a: MutableSequence, left: int, right: int) -> None:
    # a[left] ~ a[right]를 퀵정렬- 비재귀적 퀵 정렬
    range = Stack(right - left + 1)                 # 스택 생성

    range.push((left, right))

    while not range.is_empty():
        pl, pr = left, right = range.pop()      # 왼쪽, 오른쪽 커서를 꺼냄
        x = a[(left + right) // 2]              # 피벗 - 가운데 원소 

        while pl <= pr:
            while a[pl] < x:
                pl += 1
            while a[pr] > x:
                pr -= 1
            if pl <= pr:
                a[pl], a[pr] = a[pr], a[pl]
                pl += 1
                pr -= 1

        if left < pr: 
            range.push((left, pr))
        if pl < right:
            range.push((pl, right))


def quick_sort(a: MutableSequence) -> None:
    qsort(a, 0, len(a) - 1)

if __name__ == '__main__':
    print('퀵 정렬 수행')
    num = int(input('원소 수를 입력: '))
    x = [None] * num
    
    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    quick_sort(x)

    print('오름차순으로 정렬 완료')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')
