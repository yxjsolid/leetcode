
class STACK_NODE():
    def __init__(self, value):
        self.value = value
        self.cnt = 1
        self.left = None
        self.right = None
        pass

class STACK_NODE_LIST():
    def __init__(self):
        self.header = None
        self.tail = None
        self.nodeDict = {}

    def insertNode(self, value):
        node = self.header
        while node:
            if value == node.value:
                node.cnt += 1
                return node
            elif value > node.value:
                node = node.right
            else:
                newNode = STACK_NODE(value)
                newNode.right = node
                newNode.left = node.left
                if node.left:
                    node.left.right = newNode
                node.left = newNode
                return newNode
        pass


    def insert(self, value):
        if self.nodeDict.has_key(value):
            node = self.nodeDict[value]
            node.cnt += 1
        else:
            if self.header == None:
                self.header = STACK_NODE(value)
                self.tail = self.header
                newNode = self.header
            else:
                if value < self.header.value:
                    newNode = STACK_NODE(value)
                    newNode.right = self.header
                    self.header.left = newNode
                    self.header = newNode
                elif value > self.tail.value:
                    newNode = STACK_NODE(value)
                    self.tail.right = newNode
                    newNode.left = self.tail
                    self.tail = newNode
                else:
                    newNode = self.insertNode(value)

            self.nodeDict[value] = newNode
        pass

    def remove(self, value):
        node = self.nodeDict[value]
        print value, node
        node.cnt -= 1

        if node.cnt == 0:
            left = node.left
            right = node.right

            if left:
                left.right = right

            if right:
                right.left = left
            else:
                self.tail = left

    def getMin(self):
        node = self.header
        while True:
            if node == None:
                return None

            if node.cnt != 0:
                return node.value
            else:
                node = node.right

    def dump(self):
        node = self.header
        print "tail:", self.tail.value

        while True:
            if not node:
                break

            print node.value,
            node = node.right

        print

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


