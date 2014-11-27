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
        pass

    def isSameTree(self, p, q):
        if p is None and q is None:
            return True
        elif p is None:
            return False
        elif q is None:
            return False


        pList = []
        qList = []

        self.Loop(p, pList)
        self.Loop(q, qList)

        if len(pList) != len(qList):
            return False

        for i in range(len(pList)):
            if pList[i] != qList[i]:
                return False

        return True

    def isLeaf(self, node):
        if node.left or node.right:
            return False
        return True

    def Loop(self, root, valList):
        valList.append(root.val)

        if root.left:
            self.Loop(root.left, valList)
        else:
            if not self.isLeaf(root):
                valList.append(None)

        if root.right:
            self.Loop(root.right, valList)
        else:
            if not self.isLeaf(root):
                valList.append(None)






