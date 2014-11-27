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
        self.depthTmp = 0
        self._isBalanced = True

        self._MinDepth = None
        self._MaxDepth = None

    def isBalanced(self, root):
        if root is None:
            return True

        self.loopCheckBalance(root)
        return self._isBalanced

    def checkBalanced(self, root):
        if root is None:
            return True

        if root.right and root.left:
            right_max = self.maxDepth(root.right)
            left_max = self.maxDepth(root.left)

            diff = abs(right_max - left_max)
            if diff <= 1:
                return True
            return False
        else:
            if root.right is None and root.left is None:
                return True
            else:
                _max = self.maxDepth(root)
                if _max > 2:
                    return False
                return True

    def maxDepth(self, root):
        self.depthTmp = 0
        self._MaxDepth = None
        if root is None:
            return 0
        self.loop(root)
        return self._MaxDepth

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

    def setMax(self):
        if self._MaxDepth is None:
            self._MaxDepth = self.depthTmp
        else:
            self._MaxDepth = max(self.depthTmp, self._MaxDepth)

    def isLeaf(self, node):
        if node.left or node.right:
            return False
        return True

    def loop(self, root):
        self.depthTmp += 1
        if self.isLeaf(root):
            self.setMin()
            self.setMax()

        if root.left:
            self.loop(root.left)

        if root.right:
            self.loop(root.right)

        if self.depthTmp > 1:
            self.depthTmp -= 1


    def loopCheckBalance(self, root):
        if not self._isBalanced:
            return

        if self.checkBalanced(root):
            pass
        else:
            self._isBalanced = False

        if root.left:
            self.loopCheckBalance(root.left)

        if root.right:
            self.loopCheckBalance(root.right)
