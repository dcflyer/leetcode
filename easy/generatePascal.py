# -*- coding: utf-8 -*-
"""
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return 
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

@author: n609874
"""
class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        rows = []
        row = []
        for i in xrange(1, numRows+1):
            row.append(1)
            for j in xrange(i-2, 0, -1):
                row[j] = row[j] + row[j-1]
            # use deep copy
            # WRONG !!! rows.append(row[:])
            rows.append(row[:])
        return rows

if __name__ == "__main__":
    test = Solution()    
    print test.generate(5)
                
            
