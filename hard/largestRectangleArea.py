# -*- coding: utf-8 -*-
"""
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, 
find the area of largest rectangle in the histogram.

Given height = [2,1,5,6,2,3],
return 10.

@author: Dennis
"""

class Solution:
    # @param height, a list of integer
    # @return an integer
    def largestRectangleArea(self, height):
        maxArea = 0
        if not height: return maxArea
        height.append(0)
        
        i = 0
        stack = []
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
    print test.largestRectangleArea([2,1,5,6,2,3])
        