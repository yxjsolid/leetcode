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

class INFO_NODE:
    def __init__(self, val):
        self.val = val
        self.posList = [] #level, (0, -1, 1)[left,root, right]
        pass

    def updatePos(self, level, pos):
        info = [level, pos]
        if info not in self.posList:
            self.posList.append(info)


    def dump(self):

        print "val:", self.val
        for pos in self.posList:
            level , p = pos
            print "level", level, p


    def getPosCnt(self):
        self.dump()
        return len(self.posList)


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


    def check(self, n):
        newUniqueTree = []
        if n == 1:
            self.uniqueTree = [[1]]
        else:
            for serial in self.uniqueTree:
                #print "serial",serial
                num = len(serial)

                newRow = serial[:]
                newRow.insert(0, n)
                newUniqueTree.append(newRow)

                newRow = serial[:]
                newRow.insert(num, n)
                newUniqueTree.append(newRow)


                for i in range(num + 1):
                    if i == 0 or i == num:
                        continue
                    else:
                        newRow = serial[:]
                        newRow.insert(i, n)

                        root = buildBSTree(newRow, None)
                        self.getSerial(root)

                        #print "check serial:", self.serial

                        if self.serial not in newUniqueTree:
                            newUniqueTree.append(newRow)

            self.uniqueTree = newUniqueTree

        for row in self.uniqueTree:

            print row
        print

    def numTrees1(self, n):
        for i in range(1, n + 1):
            self.check(i)
        return len(self.uniqueTree)




    def numTrees(self, n):
        serialList = genTreeSerialList(n)

        for i in range(n):
            infoNode = INFO_NODE(i+1)
            self.infoNodeList.append(infoNode)

        for serial in serialList:
            root = buildBSTree(serial, self.infoNodeList)
            pass


        cnt = 0
        for i in range(n):
            node = self.infoNodeList[i]
            tmp = node.getPosCnt()
            cnt = max(cnt, tmp)

        return cnt


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
