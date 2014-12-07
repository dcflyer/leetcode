# -*- coding: utf-8 -*-
"""
Created on Tue Nov  4 14:23:33 2014
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility) 

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows: 

string convert(string text, int nRows);convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR". 

@author: n609874
"""
class Solution:
    # @return a string
    def convert(self, s, nRows):
#       WRONG, consider the case when size == 0, and null string
        if not s or nRows <= 1: return s
        res = ""
        size = 2*nRows - 2
        for i in xrange(nRows):
            j = i
            while j < len(s):
                res += s[j]
                if i != 0 and i != nRows -1 and j + size - 2*i < len(s):
                    res += s[j + size - 2*i]
                j += size
        return res

if __name__ == "__main__":
    test = Solution()
#    print test.convert("PAYPALISHIRING", 3)
    print test.convert("A", 1)
