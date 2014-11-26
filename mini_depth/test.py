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
    root = TreeNode(5)

    root7 = TreeNode(7)
    root2 = TreeNode(2)
    root1 = TreeNode(1)

    root11 = TreeNode(11)
    root13= TreeNode(13)
    root4_1 = TreeNode(4)

    root11.left = root7
    root11.right = root2
    root4_1.right = root1


    root4_0 = TreeNode(4)
    root8 = TreeNode(8)
    root4_0.left = root11
    root8.left = root13
    root8.right = root4_1

    root.left = root4_0
    root.right = root8

    return root


"""
    -2
 #      -3

"""

def buildTree2():
    root = TreeNode(1)

    #aaa = TreeNode("-1")
    bb = TreeNode(2)

    #root.left = bb
    root.right = bb

    return root



def buildTree3():
    root = TreeNode(1)
    return root


def dumpTree(node):
    if node.left:
        dumpTree(node.left)

    if node.right:
        dumpTree(node.right)


def buildTree(treeIn):
    nodeList = []
    elementCnt = 1
    length = len(treeIn)
    elemIndex = 0

    while True:
        elemList = treeIn[elemIndex : elementCnt + elemIndex]
        if len(elemList) == 0:
            break

        row = []
        for elem in elemList:
            if elem == "x":
                node = None
            else:
                node = TreeNode(elem)
            row.append(node)

        nodeList.append(row)
        elemIndex += elementCnt
        elementCnt *= 2

    root = None
    length = len(nodeList)

    for i in range(length):
        if i != length -1:
            raw1 = nodeList[i]
            raw2 = nodeList[i+1]

            index = 0
            for node in raw1:
                if root is None:
                    root = node
                node.left = raw2[index]
                node.right = raw2[index+1]
                index += 2


    for raw in nodeList:
        for node in raw:
            if node is None:
                print "#",
            else:
                print node.val,
        print

    #dumpTree(root)
    return root




if __name__ == "__main__":
    aa = [3,9,20,"x","x",15,7]

    root = buildTree(aa)

    s = Solution()
    mmm = s.minDepth(root)

    print "mindepth:", mmm



