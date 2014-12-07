# -*- coding: utf-8 -*-
"""
Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing all ones and return its area.

@author: Dennis
"""

class Solution:
    # @param matrix, a list of lists of 1 length string
    # @return an integer
    def maximalRectangle(self, matrix):
        maxArea = 0
        if not matrix: return maxArea
        histogram = [0]*len(matrix[0])
        for i in xrange(len(matrix)):
            for j in xrange(len(matrix[i])):
#                WRONG !!!
#                if '1' == matrix[i][j]:
#                    histogram[j] += 1
                histogram[j] = histogram[j] + 1 if '1' == matrix[i][j] else 0
            maxArea = max(maxArea, self.largestRectangleArea(histogram))
        return maxArea
    
    def largestRectangleArea(self, height):
        maxArea = 0
        if not height: return maxArea
        height.append(0)        
        stack = []
        i = 0
        while i < len(height):
            if not stack or height[stack[-1]] <= height[i]:
                stack.append(i)
                i += 1
            else:
                t = stack.pop()
                maxArea = max(maxArea, height[t] * \
                    (i if not stack else i - stack[-1] - 1))
        return maxArea

if __name__ == "__main__":
    test = Solution()
    matrix = [ ['0', '0', '0', '1'], 
               ['1', '1', '1', '0'],
               ['0', '1', '1', '0'],
               ['1', '0', '0', '1']]
    print test.maximalRectangle(matrix)
        