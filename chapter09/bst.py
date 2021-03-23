# 이진 검색 트리 구현하기

from __future__ import annotations
from typing import Any, Type

class Node:
    # 이진 검색 트리의 노드
    def __init__(self, key: Any, value: Any, left : Node = None, right: Node = None):
        # 생성자
        self.key = key
        self.value = value
        self.left = left
        self.right = right

class BinarySearchTree:
    # 이진 검색 트리 

    def __init__(self):
        # 초기화
        self.root = None

    def search(self, key: Any) -> Any:
        # 키가 key인 노드 검색
        p = self.root
        while True:
            if p is None:
                return None
            if key == p.key:
                return p.value
            elif key < p.key:
                p = p.left
            else:
                p = p.right 
