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
        self.err = False
        pass

    def isValidBST(self, root):
        self.root = root
        if root is None:
            return True

        self.Loop(root, None)

        if self.err:
            return False
        return True

    def check(self, root, parent):
        if root == parent.left:
            if root.tMax >= parent.val:
                return False
        elif root == parent.right:
            if root.tMin <= parent.val:
                return False

        return True

    def Loop(self, root, parent):
        if self.err:
            return

        root.tMin = root.val
        root.tMax = root.val
        if root.left:
            if root.left.val >= root.val:
                self.err = True
                return
            self.Loop(root.left, root)

        if parent:
            parent.tMax = max(root.tMax, parent.tMax)
            parent.tMin = min(root.tMin, parent.tMin)

        if root.right:
            if root.right.val <= root.val:
                self.err = True
                return
            self.Loop(root.right, root)

        if parent:
            parent.tMax = max(root.tMax, parent.tMax)
            parent.tMin = min(root.tMin, parent.tMin)

        if parent:
            if self.check(root, parent):
                pass
            else:
                self.err = True
                return