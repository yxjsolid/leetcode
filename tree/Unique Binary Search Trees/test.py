__author__ = 'xyang'
import time
from solution import *
from tree.treeCommon import *





def test(n):




    tt = time.time()
    s = Solution()
    unique = s.numTrees(n)
    #tt = time.time()
    #for i in range(1, 13):
    #    unique = s.numTrees(i)
    #print time.time() - tt
    return unique


    #print "unique", unique

if __name__ == "__main__":
    treeIn = [3,1,5,0,2,4,6,"x","x","x",3]


    tt = time.time()

    #test(5)

    reslut = [1, 2, 5, 14, 42, 132, 429, 1430, 4862, 16796, 58786, 208012]


    for i in range(12, 13):
        r = test(i)
        if r != reslut[i -1]:
            print "n: ", i,
            print "correct:", reslut[i -1],
            print "error:", r

    print time.time() - tt


    """
1 1
2 2
3 5
4 14
5 42
6 132
7 429
8 1430
9 4862
10 16796
11 58786
12 208012
        """