from typing import List

class Node:
    __slots__ = ('left_char', 'right_char', 'left_len', 'right_len', 'max_len', 'size')
    def __init__(self, left_char, right_char, left_len, right_len, max_len, size):
        self.left_char = left_char
        self.right_char = right_char
        self.left_len = left_len
        self.right_len = right_len
        self.max_len = max_len
        self.size = size

class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        n = len(s)
        self.s = list(s)
        self.tree = [None] * (4 * n)

        def merge(left: Node, right: Node) -> Node:
            if not left: return right
            if not right: return left
            size = left.size + right.size
            max_len = max(left.max_len, right.max_len)
            left_len = left.left_len
            right_len = right.right_len
            if left.right_char == right.left_char:
                max_len = max(max_len, left.right_len + right.left_len)
                if left.left_len == left.size:          
                    left_len = left.size + right.left_len
                if right.right_len == right.size:      
                    right_len = right.size + left.right_len
            return Node(left.left_char, right.right_char, left_len, right_len, max_len, size)

        def build(idx, l, r):
            if l == r:
                c = self.s[l]
                self.tree[idx] = Node(c, c, 1, 1, 1, 1)
                return
            mid = (l + r) // 2
            build(2*idx, l, mid)
            build(2*idx+1, mid+1, r)
            self.tree[idx] = merge(self.tree[2*idx], self.tree[2*idx+1])

        def update(idx, l, r, pos, c):
            if l == r:
                self.s[pos] = c
                self.tree[idx] = Node(c, c, 1, 1, 1, 1)
                return
            mid = (l + r) // 2
            if pos <= mid:
                update(2*idx, l, mid, pos, c)
            else:
                update(2*idx+1, mid+1, r, pos, c)
            self.tree[idx] = merge(self.tree[2*idx], self.tree[2*idx+1])

        build(1, 0, n-1)
        res = []
        for i, c in enumerate(queryCharacters):
            update(1, 0, n-1, queryIndices[i], c)
            res.append(self.tree[1].max_len)
        return res