# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> list[TreeNode | None]:
        from functools import lru_cache

        @lru_cache(maxsize=None)
        def build(lo: int, hi: int):
           
            if lo > hi:
                return [None]

            trees = []
            for root_val in range(lo, hi + 1):
                left_trees = build(lo, root_val - 1)
                right_trees = build(root_val + 1, hi)

                for left in left_trees:
                    for right in right_trees:
                        trees.append(TreeNode(root_val, left, right))
            return trees

        return build(1, n)