# -*- coding: utf-8 -*-
"""
Given an integer, convert it to a roman numeral. 

Input is guaranteed to be within the range from 1 to 3999.

@author: n609874
"""

# I = 1;
# V = 5;
# X = 10;
# L = 50;
# C = 100;
# D = 500;
# M = 1000;
# start from 1,4,5,9 and then repeat

class Solution:
    # @return a string
    def intToRoman(self, num):
        roman = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        digits = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

        res = ""
        for i in xrange(len(digits)):
#       WRONG!!!     while num > digits[i]
            while num >= digits[i]:
                num -= digits[i]
                res += roman[i]

        return res

if __name__ == "__main__":
    test = Solution()
    numList = [4,7,13,102,2031]
    for i in numList:
        print i, test.intToRoman(i)