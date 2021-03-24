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
                
     def add(self, key: Any, value: Any) -> bool:
        # 키가 key이고 값이 value인 노드 삽입

        def add_node(node: Node, key: Any, value: Any) -> None:
            # node를 루트로 하는 서브트리에 키가 key이고 값이 value인 노드 삽입
            if key == node.key:
                return False
            elif key < node.key:
                if node.left is None:
                    node.left = Node(key, value, None, None)
                else:
                    add_node(node.left, key, value)
            else:
                if node.right is None:
                    node.right = Node(key, value, None, None)
                else:
                    add_node(node.right, key, value)
            return True
        
        if self.root is None:
            self.root = Node(key, value, None, None)
            return True
        else:
            return add_node(self.root, key, value)
