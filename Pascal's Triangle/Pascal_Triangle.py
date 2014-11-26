__author__ = 'xyang'

class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        allRow = []

        for row in range(numRows):
            #print row
            raw = []
            for i in range(0, row+1):
                if i == 0 or i == row:
                    raw.append(1)
                else:
                    lastRow = allRow[row - 1]
                    val = lastRow[i] + lastRow[i-1]
                    raw.append(val)
            allRow.append(raw)

        return allRow
        pass
