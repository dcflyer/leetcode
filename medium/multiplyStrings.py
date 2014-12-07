# -*- coding: utf-8 -*-
"""
Given two numbers represented as strings, return multiplication of the numbers as a string.

Note: The numbers can be arbitrarily large and are non-negative.

@author: n609874
"""

class Solution:
    # @param num1, a string
    # @param num2, a string
    # @return a string
    def multiply(self, num1, num2):
        res = ""
        if not num1 or not num2: return res
        if num1[0] == '0' or num2[0] == '0': return "0"

        carry = 0   
        n1, n2 = len(num1), len(num2)
        for i in xrange(n1 + n2 - 1):
            for j in xrange(n1):
                if i >= j and n2 - 1 - (i - j) >= 0:
                    carry += int(num1[n1 - 1 - j])*int(num2[n2 - 1 - (i - j)])
            res = str(carry%10) + res
            carry /= 10
        
        if carry > 0:
            res = str(carry) + res
        
        return res
        
if __name__ == "__main__":
    test = Solution()
    print test.multiply("12345", "10")
    