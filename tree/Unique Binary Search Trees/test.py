__author__ = 'xyang'
import time
from solution import *
from tree.treeCommon import *

class MyNode():
    def __init__(self, val):
        self.val = val
        self.leftSerial = []
        self.rightSerial = []




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

def genTreeSerialList1(n):
    serialList = []
    for i in range(1, n+1):
        serialList = appendResult(serialList, i)
        #print serialList

    # cnt = 0
    # for row in serialList:
    #     if row[0] == 2:
    #         cnt +=1
    #         print row
    # print cnt
    return serialList




def handleSerial(val, serial):

    length = len(serial)
    if serial[0] != val:
        return

    if length%2:
        end = length
    else:
        end = length - 1

    #print "\nserial in:", serial
    for i in range(1, end, 2):
        a = serial[i]
        b = serial[i+1]
        if a > val and b > val or a < val and b < val:
            pass
        else:
            ll = [a,b]
            ll.sort()
            serial[i] = ll[0]
            serial[i+1] = ll[1]

    #print "serial out:", serial
    return serial


def handleList(val, serialList):
    result = []

    for serial in serialList:
        ll = handleSerial(val, serial)

        if ll and ll not in result:
            result.append(ll)

    for l in result:
        print l

    #print serialList



def test(n):

    s = Solution()
    unique = s.numTrees(n)

    print "unique", unique

if __name__ == "__main__":
    treeIn = [3,1,5,0,2,4,6,"x","x","x",3]

    val = 1


    n = 4
    serialList = genTreeSerialList1(n)

    for i in range(1, n + 1):

        handleList(i, serialList)

    #test(3)

    #genTreeSerialList(9)