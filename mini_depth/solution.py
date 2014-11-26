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
    def minDepth(self, root):
        self.depthTmp = 0
        self._MinDepth = None
        if root is None:
            return 0

        self.loop(root)
        return self._MinDepth

    def setMin(self):
        if self._MinDepth is None:
            self._MinDepth = self.depthTmp
        else:
            self._MinDepth = min(self.depthTmp, self._MinDepth)


    def isLeaf(self, node):
        if node.left or node.right:
            return False
        return True

    def loop(self, root):
        self.depthTmp += 1
        #print root.val, self.depthTmp

        if self.isLeaf(root):
            self.setMin()

        if root.left:
            self.loop(root.left)

        if root.right:
            self.loop(root.right)

        if self.depthTmp > 1:
            self.depthTmp -= 1

        #print "aaaa"



