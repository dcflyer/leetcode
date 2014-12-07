# -*- coding: utf-8 -*-
"""
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). 
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). 
Find two lines, which together with x-axis forms a container, such that the container contains the most water. 

Note: You may not slant the container. 

@author: n609874
"""
class Solution:
    # @return an integer
    def maxArea(self, height):
        if len(height) <= 1: return 0
        
        maxarea = 0
        i = 0; j = len(height) - 1
        while i < j:
            if height[i] <= height[j]:
                area = height[i]*(j - i)
                i += 1
            else:
                area = height[j]*(j - i)
                j -= 1
            if area > maxarea: maxarea = area
        return maxarea

if __name__ == "__main__":
    test = Solution()
    print test.maxArea([2,4,1,3])