# -*- coding: utf-8 -*-
"""
Given an array and a value, remove all instances of that value in place and return the new length. 

The order of elements can be changed. It doesn't matter what you leave beyond the new length. 

@author: n609874
"""
class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer

#    do not try from both front and end
#    def removeElement(self, A, elem):
#        n = len(A)
#        i = 0; j = n - 1
#        while i <= j:
    def removeElement(self, A, elem):
        i = 0; j = 0
        while j < len(A):
            if A[j] != elem:
                A[i] = A[j]
                i = i + 1
            j = j + 1
        return i
    
if __name__ == "__main__":
      
    test = Solution()
    A = [2,3,4,5,1,6,4,3,2,4]
    print test.removeElement(A, 3)
    A = [2,3,4,5,1,6,4,3,2,4]  
    print test.removeElement(A, 4)
    
            
               
                
        
