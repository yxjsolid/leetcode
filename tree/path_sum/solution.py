__author__ = 'xyang'

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def __init__(self):
        self.nodeList = []
        self.currentNode = None
        self.tmpSum = 0
        self.toCheck = 0

    def pushNode(self, node):
        self.nodeList.append(node)
        self.tmpSum += node.val

    def popNode(self):
        if len(self.nodeList):
            node = self.nodeList.pop()
            self.tmpSum -= node.val
            return node
        return None

    def forward(self, cNode):
        if cNode.left:
            cNode = cNode.left
            self.pushNode(cNode)
        elif cNode.right:
            cNode = cNode.right
            self.pushNode(cNode)
        else:
            return None
        return cNode

    def backward(self):
        self.popNode()
        length = len(self.nodeList)
        if length > 0:
            return self.nodeList[length -1]
        else:
            return None
        pass

    def loop(self):
        currentNode = self.root
        while True:
            nextNode = self.forward(currentNode)
            if nextNode is None:
                if self.tmpSum == self.toCheck:
                    return True

                while True:
                    lastNode = self.backward()
                    if lastNode:
                        if lastNode.right == currentNode or lastNode.right is None:
                            if lastNode == self.root:
                                return False
                            pass
                            currentNode = lastNode
                        else:
                            currentNode = lastNode
                            currentNode.left = None
                            break
                    else:
                        #is root
                        return False
                        pass
                pass
            else:
                currentNode = nextNode

    def hasPathSum(self, root, sum):
        if root is None:
            return False

        self.toCheck = sum
        self.root = root
        self.currentNode = root
        self.pushNode(self.root)
        self.tmpSum = root.val
        return self.loop()


    def dump(self):
        aa = []

        node = self.currentNode
        while True:
            if node is None:
                break

            aa.append(node.val)
            node = node.parent

        aa.reverse()
        print aa, self.tmpSum




        pass


