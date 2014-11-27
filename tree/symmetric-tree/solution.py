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
        self.leftList = []
        self.rightList =[]
        pass

    def isSymmetric(self, root):
        if root is None:
            return True

        self.leftLoop(root)
        self.rightLoop(root)

        if len(self.leftList) != len(self.rightList):
            return False

        for i in range(len(self.rightList)):
            if self.leftList[i] != self.rightList[i]:
                return False
        return True
        pass



    def isLeaf(self, node):
        if node.left or node.right:
            return False
        return True

    def leftLoop(self, root):
        self.leftList.append(root.val)

        if root.left:
            self.leftLoop(root.left)
        else:
            if not self.isLeaf(root):
                self.leftList.append(None)

        if root.right:
            self.leftLoop(root.right)
        else:
            if not self.isLeaf(root):
                self.leftList.append(None)


    def rightLoop(self, root):
        self.rightList.append(root.val)

        if root.right:
            self.rightLoop(root.right)
        else:
            if not self.isLeaf(root):
                self.rightList.append(None)

        if root.left:
            self.rightLoop(root.left)
        else:
            if not self.isLeaf(root):
                self.rightList.append(None)





