__author__ = 'xyang'
import time
from solution import *
from tree.treeCommon import *


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


    for row in serialList:
        print row

    return serialList

def test(n):

    s = Solution()
    unique = s.numTrees(n)

    print "unique", unique

if __name__ == "__main__":
    treeIn = [3,1,5,0,2,4,6,"x","x","x",3]

    #genTreeSerialList(4)

    test(4)

    #genTreeSerialList(9)