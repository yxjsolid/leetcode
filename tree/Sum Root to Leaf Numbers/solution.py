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
    def __init__(self):
        self.sum = 0
        self.result = 0


    def loop(self, root):
        self.sum = self.sum*10 + root.val


        if root.left:
            self.loop(root.left)

        if root.right:
            self.loop(root.right)


        if root.left is None and root.right is None:
            self.result += self.sum


        self.sum = (self.sum - root.val) /10


    def sumNumbers(self, root):
        if root is None:
            return 0
        self.loop(root)
        return self.result




