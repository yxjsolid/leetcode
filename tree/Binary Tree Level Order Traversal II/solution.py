__author__ = 'xyang'

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # @param root, a tree node
    # @return an integer
    def __init__(self):
        self.level = 0
        self.result = []

        pass

    def levelOrderBottom(self, root):
        if root is None:
            return self.result

        self.Loop(root)
        return self.result

    def insert(self, val):
        length = len(self.result)

        if self.level == length:
            self.result.insert(0, [val])
        else:
            self.result[length - 1 - self.level].append(val)

    def Loop(self, root):
        self.insert(root.val)
        self.level += 1

        if root.left:
            self.Loop(root.left)

        if root.right:
            self.Loop(root.right)

        self.level -= 1

