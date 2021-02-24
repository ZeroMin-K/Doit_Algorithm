# 힙 정렬 알고리즘 구현

from typing import MutableSequence

def heap_sort(a: MutableSequence) -> None:
    # 힙정렬

    def down_heap(a: MutableSequence, left: int, right: int) -> None:
        # a[left] ~ a[right] 를 힙으로 만들기
        temp = a[left]      # 루트

        parent = left
        while parent < (right+1) // 2:
            cl = parent * 2 + 1     # 왼쪽 자식
            cr = cl + 1             # 오른쪽 자식
            child = cr if cr <= right and a[cr] > a[cl] else cl     # 큰 값 선택
            if temp >= a[child]:
                break
            a[parent] = a[child]
            parent = child
        a[parent] = temp

    n = len(a)

    for i in range((n-1) // 2, -1, -1):         #a[i] ~ a[n-1]을 힙으로 만들기
        down_heap(a, i, n-1)

    for i in range(n-1, 0, -1):
        a[0], a[i] = a[i], a[0]                 # 최댓값인 a[0]와 마지막 원소 교환
        down_heap(a, 0, i-1)                    # a[0] ~ a[i-1]을 힙으로 만들기

if __name__ == '__main__':
    print('힙 정렬 수행')
    num = int(input('원소 수 입력: '))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    heap_sort(x)

    print('오름차순으로 정렬')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')
