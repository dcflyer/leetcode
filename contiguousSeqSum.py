# -*- coding: utf-8 -*-
"""
Given an unsorted sequence and a target, check if there is a contiguous sequence in sequence 
which sums to the target.

@author: Dennis
"""

class Solution:
    # @param l, a list of integer
    # @param target, an integer
    # @return a list

#   This code doesn't return all subseq !!!
#   Doesn't deal with 0 in sequence. To solve it, the value in hashmap should be a list, not a number
    def contiguousSeqSum(self, l, target):
        if not l: return False
        
        res = []
        cumSum = [0]*(len(l) + 1)
        for i in xrange(len(l)):
            cumSum[i + 1] = cumSum[i] + l[i]
        
        hashmap = {}
        for i in xrange(len(cumSum)):
            if cumSum[i] in hashmap:
                res.append((hashmap[cumSum[i]] + 1, i))
            else:
                hashmap[cumSum[i] + target] = i
        
#        the indices in the return results are not based on 0
        return res

if __name__ == "__main__":
    test = Solution()
    print test.contiguousSeqSum([-1, 4, 1, 0, -2, -3, 7], 2)
        