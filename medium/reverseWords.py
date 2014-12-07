# -*- coding: utf-8 -*-
"""
Given an input string, reverse the string word by word.

For example,
Given s = "the sky is blue",
return "blue is sky the".

@author: Dennis
"""

class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        if not s: return s
        
        rev, word = "", ""
        for i in xrange(len(s)):
            if " " == s[i]:
                if word:
                    rev = word + " " + rev
                    word = ""
            else:
                word += s[i]
        if word:
            rev = word + " " + rev
        return rev[:-1]

# typical Python solution   
#    def reverseWords(self, s):        
#        return ' '.join(s.split()[::-1])
    
if __name__ == "__main__":
    test = Solution()
    print test.reverseWords("the sky is blue")
    print test.reverseWords("1    ")
    print test.reverseWords("a")