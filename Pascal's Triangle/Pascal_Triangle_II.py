__author__ = 'xyang'

class Solution:
    # @return a list of lists of integers
    def getRow(self, rowIndex):
        lastRow = None
        for row in range(rowIndex+1):
            raw = []
            for i in range(0, row + 1):
                if i == 0 or i == row:
                    raw.append(1)
                else:
                    val = lastRow[i] + lastRow[i-1]
                    raw.append(val)
            lastRow = raw

        return lastRow
        pass

if __name__ == "__main__":
    s = Solution()
    print s.getRow(1)
    print s.getRow(2)
    print s.getRow(3)
    print s.getRow(4)
    print s.getRow(5)