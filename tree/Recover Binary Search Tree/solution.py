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
    def nodeSwap(self, node1, node2):
        l = node1.val
        r = node2.val
        node1.val = r
        node2.val = l
        self.done = True



    def loop(self, root):
        if self.done:
            return None

        lMinNode = root
        lMaxNode = root
        if root.left:
            r = self.loop(root.left)
            if r:
                lMinNode, lMaxNode = r

        rMinNode = root
        rMaxNode = root
        if root.right:
            r = self.loop(root.right)
            if r:
                rMinNode, rMaxNode = r


        if lMinNode.val > rMaxNode.val:
            self.nodeSwap(lMinNode, rMaxNode)
        elif lMaxNode.val > root.val:
            self.nodeSwap(lMaxNode, root)
        elif rMinNode.val < root.val:
            self.nodeSwap(rMinNode, root)

        return lMinNode, rMaxNode


    def recoverTree(self, root):
        self.done = False

        self.loop(root)
        return root



