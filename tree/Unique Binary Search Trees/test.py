__author__ = 'xyang'
import time
from solution import *
from tree.treeCommon import *



def genAllN(n):
    nL = []
    for i in range(n):
        nL.append(i+1)
    print nL
    newNL = nL[:]

    for j in range(n):
        start = newNL.pop(0)
        for i in range(n -1):
            tmp = newNL[:]
            tmp.insert(i+1, start)

            if j == n - 1 and i == n - 2:
                pass
            else:
                print tmp

        newNL = tmp[:]




def test(n):

    s = Solution()
    unique = s.numTrees(n)

    print "unique", unique

if __name__ == "__main__":
    treeIn = [3,1,5,0,2,4,6,"x","x","x",3]

    test(3)
