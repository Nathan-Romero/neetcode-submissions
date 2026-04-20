# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        # Returns height
        def dfs(node):
            if not node:
                return 0

            print(f"entered node: {node.val}")

            nonlocal res
            left, right = dfs(node.left), dfs(node.right)
            print(f"current node: {node.val}, left: {left}, right: {right}")

            # set res to max of itself and current diameter (left + right)
            res = max(res, left + right)
            print(f"res: {res}")

            # return height (max of left and right subtrees) + 1 for current node
            return 1 + max(left, right)

        dfs(root)

        return res