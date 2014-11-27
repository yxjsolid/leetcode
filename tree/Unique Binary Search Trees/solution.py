class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTREE_GEN():
    def __init__(self, serial):
        self.serial = serial
        self.root = None
        self.gen()

    def gen(self):
        for val in self.serial:
            if self.root is None:
                self.root = TreeNode(val)
            else:
                self.insert(val)

    def insert(self, val):
        curNode = self.root
        nextNode = None

        while True:
            if val > curNode.val:
                nextNode = curNode.right
                if nextNode is None:
                    curNode.right = TreeNode(val)
                    return
                else:
                    curNode = nextNode
            else:
                nextNode = curNode.left
                if nextNode is None:
                    curNode.left = TreeNode(val)
                    return


def buildBSTree(treeIn):
    tree = BSTREE_GEN(treeIn)
    return tree.root


def genTreeSerialList(n):
    result = []
    newNL = []
    for i in range(n):
        newNL.append(i+1)

    result.append(newNL)


    newNL = newNL[:]
    for j in range(n):
        start = newNL.pop(0)
        for i in range(n -1):
            tmp = newNL[:]
            tmp.insert(i+1, start)
            if j == n - 1 and i == n - 2:
                pass
            else:
                result.append(tmp)

        newNL = tmp[:]

    print result
    return result


class Solution:
    # @param root, a tree node
    # @return an integer
    def __init__(self):
        self.err = False
        self.serial = ""
        self.validDict ={}
        pass

    def numTrees(self, n):
        self.treeSerialList = genTreeSerialList(n)

        cnt = 0
        for serial in self.treeSerialList:
            root = buildBSTree(serial)
            print "serialin", serial
            if self.isValidBST(root):
                print "serial", self.serial
                if self.validDict.has_key(self.serial):
                    pass
                else:
                    self.validDict[self.serial] = 1
                    cnt += 1


        return cnt


    def isValidBST(self, root):
        self.root = root
        self.err = False
        self.serial = ""
        if root is None:
            return True

        self.Loop(root, None)

        if self.err:
            return False
        return True

    def check(self, root, parent):
        if root == parent.left:
            if root.tMax >= parent.val:
                return False
        elif root == parent.right:
            if root.tMin <= parent.val:
                return False

        return True

    def Loop(self, root, parent):
        self.serial += str(root.val)

        if self.err:
            return

        root.tMin = root.val
        root.tMax = root.val
        if root.left:
            if root.left.val >= root.val:
                self.err = True
                return
            self.Loop(root.left, root)

        if parent:
            parent.tMax = max(root.tMax, parent.tMax)
            parent.tMin = min(root.tMin, parent.tMin)

        if root.right:
            if root.right.val <= root.val:
                self.err = True
                return
            self.Loop(root.right, root)

        if parent:
            parent.tMax = max(root.tMax, parent.tMax)
            parent.tMin = min(root.tMin, parent.tMin)

        if parent:
            if self.check(root, parent):
                pass
            else:
                self.err = True
                return