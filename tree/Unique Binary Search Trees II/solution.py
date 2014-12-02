import copy

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTREE_GEN():
    def __init__(self, serial):
        self.serial = serial
        self.root = None
        self.gen()

    def gen(self):
        for val in self.serial:
            if self.root is None:
                self.root = TreeNode(val)
            else:
                self.insert(val)

    def insert(self, val):
        curNode = self.root
        nextNode = None

        while True:
            if val > curNode.val:
                nextNode = curNode.right
                if nextNode is None:
                    curNode.right = TreeNode(val)
                    return
                else:
                    curNode = nextNode
            else:
                nextNode = curNode.left
                if nextNode is None:
                    curNode.left = TreeNode(val)
                    return
                else:
                    curNode = nextNode


class Solution:
    # @param root, a tree node
    # @return an integer
    def __init__(self):
        pass




    def serialAppend(self, serial, n):
        newList = []
        newList.append(serial + [n])
        newList.append([n] + serial)

        index = 0
        lastVal = serial[0]
        for val in serial:
            if val <= lastVal:
                pass
            else:
                newSerial = serial[0:index:] + [n] + serial[index:]
                newList.append(newSerial)
                lastVal = val
            index += 1
        return newList


    def generateTrees(self, n):

        if n==0:
            ret = [None]
            return ret

        if n == 1:
            return [TreeNode(1)]

        serialList = [[1]]
        for i in range(2, n+1):
            newSerialList = []
            for serial in serialList:
                newSerialList += self.serialAppend(serial, i)
            serialList = newSerialList



        nodeList = []
        for serial in serialList:
            bst = BSTREE_GEN(serial)
            nodeList.append(bst.root)

        return nodeList


    def build(self, nodes):
        n = len(nodes)
        if n == 0:
            yield None
            return
        for i in range(n):
            root = nodes[i]
            for left in self.build(nodes[:i]):
                for right in self.build(nodes[i+1:]):
                    root.left, root.right = left, right
                    yield root

    # @return a list of tree node
    def generateTrees1(self, n):
        nodes = map(TreeNode, range(1, n + 1))
        return map(copy.deepcopy, self.build(nodes))