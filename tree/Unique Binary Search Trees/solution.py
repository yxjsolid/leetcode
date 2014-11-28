class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTREE_GEN():
    def __init__(self, serial, infoNodeList = None):
        self.serial = serial
        self.infoNodeList =  infoNodeList
        self.root = None
        self.gen()

    def setInfo(self, val, level, pos):
        if self.infoNodeList:
            node = self.infoNodeList[val-1]
            node.updatePos(level, pos)

    def gen(self):
        for val in self.serial:
            if self.root is None:
                self.root = TreeNode(val)
                self.setInfo(val, 0, -1)
            else:
                self.insert(val)

    def insert(self, val):
        curNode = self.root
        nextNode = None

        level = 0
        while True:
            level += 1
            if val > curNode.val:
                nextNode = curNode.right
                if nextNode is None:
                    curNode.right = TreeNode(val)
                    self.setInfo(val, level, 1)
                    return
                else:
                    curNode = nextNode
            else:
                nextNode = curNode.left
                if nextNode is None:
                    curNode.left = TreeNode(val)
                    self.setInfo(val, level, 0)
                    return
                else:
                    curNode = nextNode




def appendResult(orig, n):

    if n == 1:
        newList = [[1]]
    else:
        newList = []
        for row in orig:
            for i in range(len(row) + 1):
                newRow = row[:]
                newRow.insert(i, n)
                newList.append(newRow)

    #for e in newList:
    #    print e
    return newList

def genTreeSerialList(n):
    serialList = []
    for i in range(1, n+1):
        serialList = appendResult(serialList, i)
        #print serialList


    #for row in serialList:
    #    print row
    return serialList

def buildBSTree(treeIn, infoNodeList):
    tree = BSTREE_GEN(treeIn, infoNodeList)
    return tree.root




class CAT_NODE(TreeNode):
    def __init__(self, val):
        TreeNode.__init__(self, val)
        self.val = val
        self.serialDict = {}
        self.level = 0
        self.leafSerialList = []
        self.leafCnt = 0

    def getNode(self, val):
        if self.serialDict.has_key(val):
            catNode = self.serialDict[val]
        else:
            catNode = CAT_NODE(val)
            self.serialDict[val] = catNode
        return catNode

    def handle(self, serialListIn):
        # print "val:", self.val,
        # print "handle:", serialListIn

        if len(serialListIn) == 2:
            a, b = serialListIn
            if (a > self.val and b > self.val) or (a < self.val and b < self.val):
                serialListIn.sort()
            else:
                pass

            if serialListIn in self.leafSerialList:
                pass
            else:
                # print "val:", self.val,
                # print "append:", serialListIn
                self.leafSerialList.append(serialListIn)
                self.leafCnt += 1
        else:
            val = serialListIn.pop()
            node = self.getNode(val)
            node.handle(serialListIn)


    def getLeafCnt(self):
        cnt = 0
        if len(self.serialDict) == 0:
            pass
        else:
            cnt = 1
            pass


        for nodeyKey in self.serialDict:
            cnt += self.serialDict[nodeyKey].getLeafCnt()
        return cnt






    def dump(self, level):
        level += 1
        if len(self.serialDict) == 0:
            self.printLeaf()
            print

        for nodeyKey in self.serialDict:
            #self.printPad(level)
            self.printVal()
            self.serialDict[nodeyKey].dump(level)
            #print self.serialDict[nodeyKey]

        return level

    def printPad(self, level):
        pad = "\t"* level
        print
        print pad,

    def printVal(self):
        if self.val:
            print self.val,

    def printLeaf(self):
        for serial in self.leafSerialList:
            print "leaf:", serial


class CAT_ROOT(CAT_NODE):
    def __init__(self, n):
        CAT_NODE.__init__(self, 0)
        for i in range(n):
            self.getNode(i + 1)


    def dump(self, n):
        for key in self.serialDict:
            node = self.serialDict[key]
            print node.val
            node.dump(1)





    pass

class Solution:
    # @param root, a tree node
    # @return an integer
    def __init__(self):
        self.err = False
        self.serial = []
        self.validDict ={}
        self.uniqueTree = []

        self.infoNodeList = []
        pass



    def numTrees(self, n):
        serialList = genTreeSerialList(n)

        root = CAT_ROOT(n)
        for serial in serialList:
            root.handle(serial)

        cnt = root.dump(0)

        cnt = root.getLeafCnt()

        print "cnt :", cnt

        pass


    def getSerial(self, root):
        self.serial = []
        if root is None:
            return True
        self.Loop(root)

    def Loop(self, root):
        self.serial.append(root.val)

        if root.left:
            self.Loop(root.left)

        if root.right:
            self.Loop(root.right)
