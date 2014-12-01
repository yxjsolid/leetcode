class Solution:
    # @param root, a tree node
    # @return an integer
    def __init__(self):
        self.resultDict = {}
        self.resultDict[1] =  [[1]]
        self.resultDict[2] = [[1,2],[2,1],]

    def serialAppend(self, serial, n):
        lastVal = serial[0]
        newList = []

        index = 0
        newList.append([n] + serial)
        newList.append(serial + [n])

        for val in serial:
            if val <= lastVal:
                pass
            else:
                new = serial[0:index:] + [n] + serial[index:]
                newList.append(new)
                lastVal = val
            index += 1
        return newList

    def gen(self, n, lastResult):
        newResult = []
        for serial in lastResult:
            newList = self.serialAppend(serial, n)
            newResult += newList
        self.resultDict[n] = newResult
        return len(self.resultDict[n])

    def numTrees(self, n):

        if n == 1:
            return 1
        if n == 2:
            return 2

        start = 1
        for i in xrange(n -1, 0, -1):
            if self.resultDict.has_key(i):
                start = i
            break

        for i in range(start + 1, n + 1):
            self.gen(i, self.resultDict[i - 1])

        return len(self.resultDict[n])
