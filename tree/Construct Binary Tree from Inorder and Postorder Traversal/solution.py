__author__ = 'xyang'

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean


    def doSerial(self,inorder, postorder):
        if len(inorder) == 1:
            rootNode = TreeNode(inorder[0])
            return rootNode

        root = postorder.pop()
        rootNode = TreeNode(root)

        for index, v in enumerate(inorder):
            if v == root:
                if index > 0:
                    rootNode.left = self.doSerial(inorder[0:index], postorder[0:index])

                if index + 1 < len(inorder):
                    rootNode.right = self.doSerial(inorder[index+1::], postorder[index::])

                return rootNode


    def buildTree(self,inorder, postorder):
        if len(inorder) == 0:
            return None

        return self.doSerial(inorder, postorder)

