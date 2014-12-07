# -*- coding: utf-8 -*-
"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:


Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.

For example,

Consider the following matrix: 

[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
Given target = 3, return true

@author: n609874
"""

class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
## 1. not binary search O(m + n)
#    def searchMatrix(self, matrix, target):
#        if not matrix: return False
#        
#        row, col = 0, len(matrix[0]) - 1
#        while row < len(matrix) and col >= 0:
#            if target == matrix[row][col]: return True
#            elif target < matrix[row][col]: col -= 1
#            else: row += 1
#        return False

# 2. 2D binary search O(log(m) + log(n))
    def searchMatrix(self, matrix, target):
        if not matrix: return False                
        
        left, right = 0, len(matrix) - 1
        
# (1) when you use the last element of each row for comparison,
# you should set row = left, because left only increases from zero, 
# when row > len(matrix) - 1, it guarantees that target is larger than the whole matrix
# if you set row = right, right only decreases from len(matrix) - 1, 
# even right = -1, the first row (left = 0) may still have target
        while left <= right:
            mid = (left + right)//2
            if target == matrix[mid][-1]: return True
            elif target < matrix[mid][-1]: right = mid - 1
            else: left = mid + 1
        
        row = left
        if row > len(matrix) - 1: return False
## (2) when you use the first element, you should set row = right   
#        while left <= right:
#            mid = (left + right)//2
#            if target == matrix[mid][0]: return True
#            elif target < matrix[mid][0]: right = mid - 1
#            else: left = mid + 1         
#        row = right
#        if row < 0: return False
        
        left, right = 0, len(matrix[0]) - 1
        while left <= right:
            mid = (left + right)//2
            if target == matrix[row][mid]: return True
            elif target < matrix[row][mid]: right = mid - 1
            else: left = mid + 1    

        return False 

## 3. convert to a sequence, binary search O(log(m + n))
#    def searchMatrix(self, matrix, target):
#        if not matrix: return False
#        
#        rowLen, colLen = len(matrix), len(matrix[0])
#        left, right = 0, rowLen*colLen - 1
#        while left <= right:
#            mid = (left + right)//2
#            row, col = mid/colLen, mid%colLen
#            if target == matrix[row][col]: return True            
#            elif target < matrix[row][col]: right = mid - 1
#            else: left = mid + 1            
#        return False                        
            
if __name__ == "__main__":
    test = Solution()
#    matrix = [
#  [1,   3,  5,  7],
#  [10, 11, 16, 20],
#  [23, 30, 34, 50]
#  ]
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
    print test.searchMatrix(matrix, 10)        
        