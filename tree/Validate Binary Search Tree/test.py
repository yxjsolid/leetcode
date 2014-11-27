__author__ = 'xyang'
import time
from solution import *
from tree.treeCommon import *


def test(treeIn):
    root = buildTree(treeIn)
    s = Solution()
    print s.isValidBST(root)


if __name__ == "__main__":
    treeIn = [3,1,5,0,2,4,6,"x","x","x",3]

    #treeIn = [5, 14, "x", 1]#false
    treeIn = [10,5,15,"x","x",6,20] #false
    #treeIn = [5, 4, "x", 1] #True
    #treeIn = [5, 2, 7, 1] #True

    #treeIn = [3,1,5,0,2,4,6] #true

    test(treeIn)

