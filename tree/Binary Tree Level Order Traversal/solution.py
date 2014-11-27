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

    def levelOrder(self, root):
        if root is None:
            return self.result

        self.Loop(root)
        return self.result

    def insert(self, val):
        if self.level == len(self.result):
            self.result.append([val])
        else:
            self.result[self.level].append(val)

    def Loop(self, root):
        self.insert(root.val)
        self.level += 1

        if root.left:
            self.Loop(root.left)

        if root.right:
            self.Loop(root.right)

        self.level -= 1

