__author__ = 'xyang'


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

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

                if node is None:
                    continue

                if index < len(raw2):
                    node.left = raw2[index]

                if index + 1 < len(raw2):
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