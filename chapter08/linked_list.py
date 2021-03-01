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
