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

    def loop(self, root, level):
        if len(self.result) <= level:
            levelArray = []
            self.result.append(levelArray)
        else:
            levelArray = self.result[level]

        if level%2:
            levelArray.insert(0, root.val)
        else:
            levelArray.append(root.val)

        level += 1
        if root.left:
            self.loop(root.left, level)

        if root.right:
            self.loop(root.right, level)


    def zigzagLevelOrder(self, root):
        self.result = []
        if root is None:
            return []
        self.loop(root, 0)
        return self.result

