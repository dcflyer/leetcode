# -*- coding: utf-8 -*-
"""
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.

@author: Dennis
"""
#（1）00：res[i]=0（无法解析，没有可行解析方式）；
#（2）10, 20：res[i]=res[i-2]（只有第二种情况成立）；
#（3）11-19, 21-26：res[i]=res[i-1]+res[i-2]（两种情况都可行）；
#（4）01-09, 27-99：res[i]=res[i-1]（只有第一种情况可行）；

class Solution:
    # @param s, a string
    # @return an integer
    def numDecodings(self, s):
        if not s or '0' == s[0]: return 0
#       WRONG !!! don't use an array, need to deal with i, i - 1, i - 2
#       when i == 1, not easy to handle
#        res = [0]*len(s)
        
        prev2, prev, curr = 1, 1, 1
        for i in xrange(1, len(s)):
            if '0' == s[i]:
                if '1' == s[i - 1] or '2' == s[i - 1]:
                    curr = prev2
                else:
                    return 0
            else:
                if '0' == s[i - 1] or s[i - 1] >= '3':
                    curr = prev
                else:
                    if s[i - 1] == '2' and s[i] >= '7':
                        curr = prev
                    else:
                        curr = prev + prev2
            prev2 = prev
            prev = curr
        
        return curr

if __name__ == "__main__":
    test = Solution()
    print test.numDecodings('12')
                
                
        