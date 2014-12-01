__author__ = 'xyang'
import time
from solution import *
from tree.treeCommon import *





def test(n):
    tt = time.time()
    s = Solution()
    #unique = s.numTrees(n)
    tt = time.time()
    for i in range(1, 13):
        unique = s.numTrees(i)
    print time.time() - tt

    print unique

    #print "unique", unique

if __name__ == "__main__":
    treeIn = [3,1,5,0,2,4,6,"x","x","x",3]


    tt = time.time()

    test(12)

    # for i in range(1, 13):
    #     test(i)
    # print time.time() - tt