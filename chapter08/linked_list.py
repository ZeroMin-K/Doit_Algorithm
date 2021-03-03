# 포인터로 연결 리스트 구현

from typing import Any, Type

class Node:
    # 연결 리스트용 노드 클래스 

    def __init__(self, data: Any = None, next: Node = None):
        # 초기화
        self.data = data
        self.next = next

class LinkedList:
    # 연결 리스트 클래스

    def __init__(self) -> None:
        # 초기화
        self.no = 0     # 노드의 개수
        self.head = None    # 머리 노드
        self.current = None # 주목 노드

    def __len__(self)-> int:
        # 연결 리스트의 노드 개수 반환
        return self.no

    def search(self, data: Any) -> int:
        # data와 값이 같은 노드 검색
        cnt = 0
        ptr = self.head
        while ptr is not None:
            if ptr.data == data:
                self.current = ptr
                return cnt
            cnt += 1
            ptr = ptr.next
        return -1

    def __contains__(self, data: Any) -> bool:
        # 연결리스트에 data가 포함되어 있는지 확인
        return self.search(data) >= 0
    
     def add_first(self, data: Any) -> None:
        # 맨앞에 노드 삽입
        ptr = self.head
        self.head = self.current = Node(data, ptr)
        self.no += 1

    def add_last(self, data: Any):
        # 맨 끝에 노드 삽입
        if self.head is None:   # 리스트가 비어있으면
            self.add_first(data)    # 맨앞에 노드 삽입
        else:
            ptr = self.head
            while ptr.next is not None:
                ptr = ptr.next
            ptr.next = self.current = Node(data, Node)
            self.no += 1
            
    def remove_first(self) -> None:
        # 머리노드 삭제
        if self.head is not None:   # 리스트가 비어 있으면
            self.head = self.current = self.head.next
        self.no -= 1

    def remove_last(self):
        # 꼬리 노드 삭제
        if self.head is not None:
            if self.head.next is None:  # 노드가 1개뿐이라면
                self.remove_first()     # 머리노드 삭제
            else:
                ptr = self.head         # 스캔 중인 노드
                pre = self.head         # 스캔 중인 노드의 앞쪽 노드

                while ptr.next is not None:
                    pre = ptr
                    ptr = ptr.next

                pre.next = None         # pre는 삭제 뒤 꼬리노드
                self.current = pre
                self.no -= 1
