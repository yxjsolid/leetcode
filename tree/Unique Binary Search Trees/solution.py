class MY_NODE():
    def __init__(self):
        self.serial = []
        self.cnt = 1

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def __init__(self):
        self.resultDict = {}
        node1 = MY_NODE()
        node1.serial = [1]

        self.resultDict[1] =  [node1]

        node2 = MY_NODE()
        node2.serial = [1,2]

        node3 = MY_NODE()
        node3.serial = [2,1]

        self.resultDict[2] = [node2,node3,]
        self.n = 1

    def serialAppend(self, node, n):
        serial = node.serial
        newNodeList = []

        index = 0

        newNode = MY_NODE()
        newNode.serial = serial + [n]
        newNodeList.append(newNode)
        newNode.cnt = node.cnt

        start = 0
        for val in serial:
            if val > serial[0]:
                serial = serial[start-1:]
                break
            start += 1
        #newList.append(serial + [n])


        lastVal = serial[0]
        for val in serial:
            if val <= lastVal:
                pass
            else:
                newNode = MY_NODE()

                newNode.serial = serial[0:index:] + [n] + serial[index:]
                newNode.cnt = node.cnt
                newNodeList.append(newNode)
                lastVal = val
            index += 1

        return newNodeList

    def gen(self, n, lastResult):
        newResult = []
        newNode = MY_NODE()
        newNode.serial = [n]
        newResult += [newNode]
        newNode.cnt = 0
        for node in lastResult:
            newNode.cnt += node.cnt
            newNodeList = self.serialAppend(node, n)
            newResult += newNodeList

        self.resultDict[n] = newResult


    def numTrees(self, n):

        self.result = {}
        self.result[0] = 1
        self.result[1] = 1
        self.result[2] = 2

        if n < 3:
            return self.result[n]

        for i in range(3, n + 1):
            a = 0
            for p in range(0, i):
                a += self.result[i - 1 - p]*self.result[p]
            self.result[i] =a

        return self.result[n]

    def numTrees1(self, n):
        if n == 1:
            return 1

        for i in range(2, n + 1):
            self.gen(i, self.resultDict[i - 1])

        cnt = 0
        for node in self.resultDict[n]:

            if node.cnt > 1:
                print node.cnt, node.serial


            cnt += node.cnt
        return cnt


    def serialAppend1(self, serial, n):
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

        if n == 1 :




        serialList = [[1,2],[2,1]]

        for i in range(1, n+1):

            for serial in serialList:
                self.serialAppend1(serial, 1)


        pass
