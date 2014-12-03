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
        self.toCheck = 0
        self.find = False

    def hasPathSum(self, root, sum):
        self.toCheck = sum
        if root is None:
            return False

        self.loop(root)
        return self.find

    def loop(self, root):
        self.sum += root.val

        if self.find:
            return

        if root.left:
            self.loop(root.left)

        if root.right:
            self.loop(root.right)

        if root.left is None and root.right is None:
            if self.sum == self.toCheck:
                self.find = True
                return
        self.sum -= root.val

