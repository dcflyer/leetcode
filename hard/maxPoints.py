# -*- coding: utf-8 -*-
"""
Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

@author: Dennis
"""

# Definition for a point
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
 
class Solution:
    # @param points, a list of Points
    # @return an integer

# for each point, there is a hashmap, easy to implement
    def maxPoints(self, points):
        if not points: return 0
       
        maxNum = 0
        hashmap = {}
        for i in xrange(len(points)):
            hashmap.clear()
            hashmap['inf'] = 0
            duplicate = 1
            for j in xrange(len(points)):
                if i == j: continue
                elif points[i].x == points[j].x and points[i].y == points[j].y:
                    duplicate += 1
                elif points[i].x == points[j].x:
                    hashmap['inf'] += 1
                else:
                    ratio = 1.0 * (points[i].y - points[j].y)/(points[i].x - points[j].x)
                    if ratio in hashmap:
                        hashmap[ratio] += 1
                    else:
                        hashmap[ratio] = 1
            maxNum = max(maxNum, max(hashmap.values()) + duplicate)
        return maxNum         
        

if __name__ == "__main__":
    test = Solution()
    print test.maxPoints([Point(0,0)])