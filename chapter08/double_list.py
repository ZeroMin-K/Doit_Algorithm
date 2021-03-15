from __future__ import annotations
from typing import Any, Type

class Node:
    # 원형 이중 연결 리스트용 노드 클래스

    def __init__(self, data: Any = None, prev: Node= None,
                        next: Node = None) -> None:
        # 초기화
        self.data = data
        self.prev = prev or self
        self.next = next or self

class DoubleLinkedList:
    # 원형 이중 연결 리스트 클래스

    def __init__(self) -> None:
        # 초기화
        self.head = self.current = Node()           # 더미 노드 생성
        self.no = 0

    def __len__(self) -> int:
        # 연결리스트 노드수 반환
        return self.no
    
    def is_empty(self) -> bool:
        # 리스트가 비어있는지 확인
        return self.head.next is self.head
