__author__ = 'xyang'

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean

    def loop(self, root):
        if root.left:
            self.loop(root.left)
        if root.right:
            self.loop(root.right)
        self.result.append(root.val)

    def postorderTraversal(self, root):
        self.result = []
        if root is None:
            return []
        self.loop(root)
        return self.result

