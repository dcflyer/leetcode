# -*- coding: utf-8 -*-
"""
Given a non-negative number represented as an array of digits, plus one to the number.

The digits are stored such that the most significant digit is at the head of the list.

@author: weichen
"""

class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
#    def plusOne(self, digits):
#        num = 0
#        for i in xrange(len(digits)):
#            num = num*10 + digits[i]
#        num = num + 1
    def plusOne(self, digits):
        if len(digits) < 1:
            return digits
        carry = 1
        i = len(digits) - 1
        while i >= 0:
            digit = (digits[i] + carry)%10
            carry = (digits[i] + carry)/10
            digits[i] = digit
            if carry == 0:
                return digits
            i = i - 1
        return [1] + len(digits)*[0]
        
if __name__ == "__main__":
    A = [0]
    B = [9,9]
    C = [1,2,3]
    test = Solution()
    print test.plusOne(A)
    print test.plusOne(B)
    print test.plusOne(C)