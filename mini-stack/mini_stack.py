
class STACK_NODE():
    def __init__(self, value):
        self.value = value
        self.cnt = 1
        pass

class STACK_NODE_LIST():
    def __init__(self):
        self.nodeList = []
        self.nodeDict = {}
        self.nodeCnt = 0

    def getValue(self, index):
        return self.nodeList[index].value

    def search(self, value):
        cnt = self.nodeCnt
        #print "node Cnt:", cnt

        lIndex = 0
        rIndex = cnt -1
        index = cnt/2
        tmp = 0

        while True:
            if value > self.getValue(index):
                if rIndex - lIndex <= 2:

                    return index + 1
                lIndex = index
                index += (rIndex - lIndex)/2
            else:
                if rIndex - lIndex <= 2:

                    return index
                rIndex = index
                index -= (rIndex - lIndex)/2

            tmp += 1
            #print tmp


    def insertNode(self, value):
        newNode = STACK_NODE(value)
        if self.nodeCnt:
            if value > self.getValue(self.nodeCnt - 1):
                self.nodeList.append(newNode)
            elif value < self.getValue(0):
                self.nodeList.insert(0, newNode)
            else:
                index = self.search(value)
                self.nodeList.insert(index, newNode)
        else:
            self.nodeList.append(newNode)

        self.nodeCnt += 1

        return newNode
        pass


    def insert(self, value):
        if self.nodeDict.has_key(value):
            node = self.nodeDict[value]
            node.cnt += 1
        else:
            newNode = self.insertNode(value)
            self.nodeDict[value] = newNode
        pass

    def remove(self, value):
        node = self.nodeDict[value]
        node.cnt -= 1

        if node.cnt == 0:
            index = self.search(value)
            self.nodeList.pop(index)
            #self.nodeList.remove(node
            self.nodeCnt -= 1
            self.nodeDict.pop(value)


    def getMin(self):
        if self.nodeCnt:
            node = self.nodeList[0]
            return node.value

        return None

    def dump(self):
        pass


class MinStack:
    def __init__(self):
        self.stack = []
        self.length = 0
        self.stackSort = STACK_NODE_LIST()

    # @param x, an integer
    # @return an integer
    def push(self, x):
        self.stack.append(x)
        self.stackSort.insert(x)
        self.length += 1

        #self.stackDict[index] =
    # @return nothing
    def pop(self):
        value = self.top()
        if value:
            self.stack.pop()
            self.stackSort.remove(value)
            self.length -= 1


    # @return an integer
    def top(self):
        if self.length > 0:
            return self.stack[self.length - 1]

        return None

    # @return an integer
    def getMin(self):
        return self.stackSort.getMin()

    def dump(self):

        self.stackSort.dump()
        print self.stack


