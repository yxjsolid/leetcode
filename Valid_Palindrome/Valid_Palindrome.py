__author__ = 'xyang'

class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):

        newString = ""
        for c in s:
            if c.isdigit() or c.isalnum() or c.isalpha():
                newString += c.lower()
        length = len(newString)
        if length == 0:
            return True

        for i in range(length/2):
            if newString[i] != newString[length - 1 - i]:
                return False

        return True

