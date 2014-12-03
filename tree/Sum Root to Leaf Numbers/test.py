__author__ = 'xyang'
import time
from solution import *


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

"""
         5
         / \
        4    8
        /   / \
       11  13  4
       / \      \
      7   2      1
"""
def buildTree1():
    root = TreeNode(1)


    root2 = TreeNode(2)


    root.left = root2

    return root


"""
    -2
 #      -3

"""

def buildTree2():
    root = TreeNode(-2)

    #aaa = TreeNode("-1")
    bb = TreeNode(-3)

    #root.left = bb
    root.right = bb

    return root


def buildTree3():#15
    root = TreeNode(1)

    node = root
    for i in range(2, 6):
        print i
        tmpNode = TreeNode(i)
        node.right = tmpNode
        node = tmpNode
    return root


def buildTree4():
    root = TreeNode(1)

    node1 = TreeNode(-2)
    node2 = TreeNode(1)
    node3 = TreeNode(-1)

    root.left = node1
    node1.left = node2
    node2.left = node3
    return root


def buildTree5():
    root = TreeNode(1)
    return root


if __name__ == "__main__":

    root = buildTree1()
    s = Solution()
    print s.sumNumbers(root)


