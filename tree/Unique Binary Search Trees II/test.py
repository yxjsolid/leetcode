__author__ = 'xyang'
import time
from solution import *
from tree.treeCommon import *





def test(n):




    tt = time.time()
    s = Solution()

    #tt = time.time()
    unique = s.generateTrees(n)
    #for i in range(1, 13):
    #    unique = s.numTrees(i)
    print time.time() - tt





    tt = time.time()
    unique = s.generateTrees1(n)
    #for i in range(1, 13):
    #    unique = s.numTrees(i)
    print time.time() - tt

    return unique


    #print "unique", unique

if __name__ == "__main__":
    test(9)