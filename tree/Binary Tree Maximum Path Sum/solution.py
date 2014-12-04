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
        if self.max is None:
            self.max = root.val

        l = 0
        r = 0
        if root.left:
            l = self.loop(root.left)

        if root.right:
            r = self.loop(root.right)

        nodeSum = root.val + l + r


        nodePathMax = max(root.val, root.val + l, root.val + r)

        self.max = max(nodeSum, self.max, nodePathMax)
        return nodePathMax


    def maxPathSum(self, root):
        self.max = None
        if root is None:
            return 0
        self.loop(root)

        return self.max


