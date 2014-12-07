# -*- coding: utf-8 -*-
"""
Determine whether an integer is a palindrome. Do this without extra space.

@author: n609874
"""

class Solution:
    # @return a boolean 
    def isPalindrome(self, x): 
        if x < 0:
            return False
        
        digit = 0
        y = x
        while y > 0:
            y /= 10
            digit += 1
        if digit < 1:
            return True
        
#        won't work for odd number, once you change digit here        
#        if digit%2 == 1:
#            digit -= 1
#        digit /= 2
#        
#        rev_x = 0
#        while digit > 0:
#            rev_x = rev_x*10 + x%10
#            x /= 10
#            digit -= 1
        rev_x = 0
        for i in xrange(digit/2):
            rev_x = rev_x*10 + x%10
            x /= 10
        if digit%2 == 1:
            x /= 10
        
        if rev_x == x:
            return True
        else:
            return False

if __name__ == "__main__":
    test = Solution()
    l = [0, 45, 123, 131, 1441]
    for i in xrange(len(l)):
        print l[i], test.isPalindrome(l[i])
    

        
