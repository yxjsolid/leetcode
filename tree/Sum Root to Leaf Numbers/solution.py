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

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean

    def loop(self, root, s):
        s = s*10 + root.val

        if root.left is None and root.right is None:
            return s

        val = 0
        if root.left:
            val = self.loop(root.left, s)

        if root.right:
            val += self.loop(root.right, s)

        return val

    def sumNumbers(self, root):
        if root is None:
            return 0
        return self.loop(root, 0)


