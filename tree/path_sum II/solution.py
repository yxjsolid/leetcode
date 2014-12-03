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
        self.toCheck = 0
        self.sum = 0
        self.serial = []
        self.resultList = []


    def loop(self, root):
        self.sum += root.val
        self.serial.append(root.val)

        if root.left:
            self.loop(root.left)

        if root.right:
            self.loop(root.right)


        if root.left is None and root.right is None:
            if self.sum == self.toCheck:
                self.resultList.append(self.serial[::])

        self.sum -= root.val
        self.serial.pop()


    def pathSum(self, root, sum):
        self.toCheck = sum
        if root is None:
            return []
        self.loop(root)
        return self.resultList




