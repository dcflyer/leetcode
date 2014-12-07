# -*- coding: utf-8 -*-
"""
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:
Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9]. 

Example 2:
Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16]. 

This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10]. 

@author: n609874
"""

# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @param newInterval, a Interval
    # @return a list of Interval
# WRONG!!! failed, make a copy of intervals should be easier
#    def insert(self, intervals, newInterval):
#        if not intervals: return [newInterval]
#        
#        for pos in xrange(len(intervals)):
#            if intervals[pos].end > newInterval.start:
#                break
#        
#        for end in xrange(pos, len(intervals)):
#            if intervals[end].start <= newInterval.end and \
#                intervals[end].end > newInterval.end:
#                break
#        
#        if intervals[pos].start <= newInterval.start:
#            newInterval.start = intervals[pos].start
#        if intervals[end].end > newInterval.end:
#            newInterval.end = intervals[end].end
#        
#        del intervals[pos:(end + 1)]
#        intervals.insert(pos, newInterval)
#        
#        return intervals

    def insert(self, intervals, newInterval):
        if not intervals: return [newInterval]
                
        res = []; i = 0
#        WRONG !!!
#        while i < len(intervals):
#            if intervals[i].end < newInterval.start:
#                res.append(intervals[i])
#                i += 1

        while i < len(intervals) and intervals[i].end < newInterval.start:
                res.append(intervals[i])
                i += 1

#        update start of new interval
        if i < len(intervals):
            newInterval.start = min(intervals[i].start, newInterval.start)
#            WRONG !!! fails in [[1,5]], [2,3] case
#            i += 1
            
        res.append(newInterval)
        
#        update end of new interval        
        while i < len(intervals) and intervals[i].start <= newInterval.end:
            newInterval.end = max(intervals[i].end, newInterval.end)
            i += 1
        
        while i < len(intervals):
            res.append(intervals[i])
            i += 1
            
        return res
                


if __name__ == "__main__":
    test = Solution()
#    l = [Interval(1,2), Interval(3,5), Interval(6,7), Interval(8,10), Interval(12,16)]
#    res = test.insert(l, Interval(4,9)) 
    l = [Interval(2,5), Interval(6,7), Interval(8,9)]
    res = test.insert(l, Interval(0,1)) 
    for s in res:
        print s.start, s.end       
    
