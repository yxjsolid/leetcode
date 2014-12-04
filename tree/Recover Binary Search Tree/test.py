__author__ = 'xyang'
import time
from solution import *


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def buildTree1():
    root = TreeNode(0)
    root2 = TreeNode(1)


    root.left = root2
    return root


def buildTree2():
    root = TreeNode(2)
    root2 = TreeNode(1)


    root.right = root2
    return root


def buildTree3():
    root = TreeNode(2)
    root1 = TreeNode(1)
    root3 = TreeNode(3)
    root.right = root1
    root.left = root3
    return root

def buildTree4():
    root = TreeNode(1)
    root1 = TreeNode(2)
    root3 = TreeNode(3)
    root.left = root1
    root.right = root3



    return root


if __name__ == "__main__":

    root = buildTree4()
    s = Solution()



    print root.val
    if root.left:
        print "left:", root.left.val

    if root.right:
        print " right:",root.right.val

    print
    tree =  s.recoverTree(root)

    print tree.val
    if tree.left:
        print "left:", tree.left.val

    if tree.right:
        print " right:",tree.right.val

