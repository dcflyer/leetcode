# -*- coding: utf-8 -*-
"""
Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18]. 

@author: n609874
"""

# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    # @param intervals, a list of Interval
    # @return a list of Interval
    def merge(self, intervals):
        res = []
        if not intervals: return res
        
        intervals.sort(key = lambda x: x.start)
        res.append(intervals[0])
        for i in xrange(1, len(intervals)):
            if intervals[i].start <= res[-1].end:
                res[-1].end = max(res[-1].end, intervals[i].end)
            else:
                res.append(intervals[i])
        return res

if __name__ == "__main__":
    test = Solution()
    l = [Interval(1,3), Interval(2,6), Interval(8,10), Interval(15,18)]
    res = test.merge(l)
    for s in res:
        print s.start, s.end
            
        
        