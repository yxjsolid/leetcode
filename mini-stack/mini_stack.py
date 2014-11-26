class MinStack:
    def __init__(self):
        self.stack = []
        self.length = 0
        self.currentMin = None
        self.minValCnt = 0

    # @param x, an integer
    # @return an integer
    def push(self, x):
        self.stack.append(x)
        self.length += 1
        if self.currentMin is None:
            self.currentMin = x
            self.minValCnt = 1
        else:
            if self.currentMin == x:
                self.minValCnt += 1
            elif x < self.currentMin:
                self.currentMin = x
                self.minValCnt = 1

        #print "\nafter push"
        #self.dump()

    def getNextMin(self):
        minVal = None
        cnt = 0
        for x in self.stack:
            if minVal is None:
                minVal = x
                cnt = 1
            else:
                if minVal < x:
                    pass
                elif minVal == x:
                    cnt +=1
                else:
                    minVal = x
                    cnt = 1

        self.currentMin = minVal
        self.minValCnt = cnt


    #self.stackDict[index] =
    # @return nothing
    def pop(self):
        value = self.top()
        if value is not None:
            self.stack.pop()
            if value == self.currentMin:
                self.minValCnt -= 1
                if self.minValCnt == 0:
                    #print "getMin"
                    self.getNextMin()
                    pass

            self.length -= 1

        #print "\nafter pop"
        #self.dump()

    # @return an integer
    def top(self):
        if self.length > 0:
            return self.stack[self.length - 1]
        return None

    # @return an integer
    def getMin(self):
        return self.currentMin

    def dump(self):
        print "dump:"
        print self.stack
        print self.currentMin, self.minValCnt
