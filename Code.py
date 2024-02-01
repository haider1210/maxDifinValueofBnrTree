# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.mini = float('inf')
        self.maxi = float('-inf')

    def solve(self, root):
        
        if not root:
            return

        self.mini = min(self.mini, root.val)
        self.maxi = max(self.maxi, root.val)

        self.solve(root.left)
        self.solve(root.right)

    def maxAncestorDiff(self, root):
        self.solve(root)
        print(self.maxi ,self.mini)
        return self.maxi - self.mini
