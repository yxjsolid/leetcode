class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []
        self.length = 0

    def pushMin(self, x):
        self.minStack.append(x)

    def popMin(self):
        self.minStack.pop()

    # @param x, an integer
    # @return an integer
    def push(self, x):
        self.stack.append(x)
        self.length += 1

        currentMin = self.getMin()
        if currentMin is None:
            self.pushMin(x)
        else:
            if currentMin >= x:
                self.pushMin(x)


    def pop(self):
        value = self.top()
        if value is not None:
            self.stack.pop()
            if value == self.getMin():
                self.popMin()

            self.length -= 1

    # @return an integer
    def top(self):
        if self.length > 0:
            return self.stack[self.length - 1]
        return None

    # @return an integer
    def getMin(self):
        length = len(self.minStack)

        if length:
            return self.minStack[length - 1]
        return None

    def dump(self):
        print "dump:"
        print self.stack
