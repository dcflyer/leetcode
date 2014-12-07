# -*- coding: utf-8 -*-
"""
Created on Thu Oct 30 11:47:22 2014

Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather all the input requirements up front. 

@author: n609874
"""

class Solution:
    # @return an integer
    def atoi(self, str):
        sign = 1
        num = 0
        INT_MAX = 2147483647; INT_MIN = -2147483648
        
        str = str.strip()
#        for i in xrange(len(str)):
#            if not str[i].isspace():
#                str = str[i:]
#                break
        if str == "": return 0
        
        if str[0] == "+" or str[0] == "-":
            if str[0] == "-": sign = -1
            str = str[1:]
        elif not str[0].isdigit():
            return 0
        
        for s in str:
            if not s.isdigit():
                break
            num = num*10 + int(s)
        
        num *= sign
        if num > INT_MAX:
            return INT_MAX
        elif num < INT_MIN:
            return INT_MIN
        else:
            return num
       

if __name__ == "__main__":
    test = Solution()
    strList = ["", "    ", "    +", "  -+ ", "-s98", "  +87so ", "-8110.2 ", 
               "+13212321323271832197311239"]

    for str in strList:
        print "string is " + str, "converted int is", test.atoi(str)
    