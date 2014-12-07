# -*- coding: utf-8 -*-
"""
Divide two integers without using multiplication, division and mod operator. 

@author: n609874
"""
class Solution:
    # @return an integer

# num=a_0*2^0+a_1*2^1+a_2*2^2+...+a_n*2^n

    def divide(self, dividend, divisor):
        if not dividend: return 0
        sign = 1
        if dividend < 0: sign = -sign
        if divisor < 0: sign = -sign        
        dividend = abs(dividend); divisor = abs(divisor)      

        if dividend < divisor: return 0        
        digits = 0
        res = 0
        
        while divisor < dividend:
            divisor <<= 1
            digits += 1
        
        while digits >= 0:
            if dividend >= divisor:
                dividend -= divisor
                res += 1<<digits
            digits -= 1
            divisor >>= 1
            
        return res*sign
        
if __name__ == "__main__":
    test = Solution()
    l = [[2,3], [35,2], [9,3], [-2,3]]
    for i in l:
        print test.divide(i[0], i[1])        
