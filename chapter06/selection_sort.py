# 단순 선택 정렬 알고리즘 구현

from typing import MutableSequence

def selection_sort(a: MutableSequence) -> None:
    # 단순 선택 정렬
    n = len(a)
    for i in range(n-1):
        min = i
        for j in range(i +1, n):
            if a[j] < a[min]:
                min = j
        a[i], a[min] = a[min], a[i]         # 정렬할 부분에서 맨 앞의 원소와 가장 작은 원소 교환 

if __name__ == '__main__':
    print('단순 선택 정렬을 수행합니다.')
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num  # 원소 수 num인 배열을 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}] : '))

    selection_sort(x)  # 배열 x를 단순 교환 정렬

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')
