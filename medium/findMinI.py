# -*- coding: utf-8 -*-
"""
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

You may assume no duplicate exists in the array.

@author: weichen
"""

class Solution:
    # @param num, a list of integer
    # @return an integer

#    def findMin(self, num):
#        if not num: return -1
#        
#        min = num[0]
#        l = 0; r = len(num) - 1
#        while l <= r:
#            m = (l + r)//2
##            WRONG !!! don't work for [2,1]. 
##            when you choose to compare left with middle,
##            with <, you cannot rule out two numbers case
##            because num[l] == num[m] occurs!!!  
##            ALWAYS COMPARE WITH RIGHT!!!   
##            num[m] == num[r] only occurs when there is one number
##            num[l] == num[m] occurs when there is one or TWO numbers
##            if num[l] < num[m]:
#            if num[l] <= num[m]:
#                min = min if min < num[l] else num[l]
#                l = m + 1
#            else:
#                min = min if min < num[m] else num[m]
#                r = m - 1
#        
#        return min
        
        
    def findMin(self, num):
        if not num: return -1
        
        min = num[0]
        l = 0; r = len(num) - 1
        while l <= r:
            m = (l + r)//2
            if num[m] < num[r]:
                min = min if min < num[m] else num[m]
                r = m - 1
            else:
                min = min if min < num[l] else num[l]
                l = m + 1
        
        return min
                
if __name__ == "__main__":
    test = Solution()
    num = [2, 1]
    print test.findMin(num)      

        
        
        