# -*- coding: utf-8 -*-
"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers. 

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order). 

The replacement must be in-place, do not allocate extra memory. 

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

@author: n609874
"""

class Solution:
    # @param num, a list of integer
    # @return a list of integer
    def nextPermutation(self, num):
        if not num: return num
        
#        find the first smaller number from right to left
        partition = -1
        for i in reversed(xrange(len(num) - 1)):
            if num[i] < num[i + 1]:
                partition = i; break;
#        find the first larger number than partition, swap them
        if partition != -1:
            for i in reversed(xrange(partition + 1, len(num))):
                if num[i] > num[partition]:
                    num[i], num[partition] = num[partition], num[i]
                    break
#        reverse the sublist after partition
        l = partition + 1; r = len(num) - 1
        while l <= r:
            num[l], num[r] = num[r], num[l]
            l += 1; r -= 1
        
        return num
            
if __name__ == "__main__":
    test = Solution()
    print test.nextPermutation([2,3,6,5,4,1])
            