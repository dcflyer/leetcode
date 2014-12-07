# -*- coding: utf-8 -*-
"""
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

For example, 
Given s = "Hello World",
return 5. 
        
@author: n609874
"""
class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        length = 0
        find = False
        for i in xrange(len(s) - 1, -1, -1):
            if s[i].isalpha():
                if 0 == length:
                    find = True
                length += 1
            elif True == find:
                return length
        
        return length

if __name__ == "__main__":
    test = Solution()
    sList = ["   fad fdai  ", "fa  ", "  dfa", "dafdf"]
    for s in sList:
        print s, test.lengthOfLastWord(s)
            
        