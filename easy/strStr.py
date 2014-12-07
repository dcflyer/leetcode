# -*- coding: utf-8 -*-
"""
Implement strStr(). 

Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack. 

Update (2014-11-02):
The signature of the function had been updated to return the index instead of the pointer. If you still see your function signature returns a char * or String, please click the reload button 兪to reset your code definition. 

@author: n609874
"""

class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return an integer

## 1. rolling hash
#    def strStr(self, haystack, needle):
#        if not haystack or not needle or len(haystack) < len(needle): return -1
#        
#        base, tempbase, L = 29, 1, len(needle)
#        
#        needleCode, hashCode = 0, 0
#        for i in reversed(xrange(L)):
#            needleCode += ord(needle[i])*tempbase
#            hashCode += ord(haystack[i])*tempbase
#            tempbase *= base
#        
#        if hashCode == needleCode: return 0
#        tempbase /= base        
#        for i in xrange(L, len(haystack)):
#            hashCode -= ord(haystack[i - L])*tempbase
#            hashCode *= base
#            hashCode += ord(haystack[i])
#            if hashCode == needleCode: return i - (L - 1)
#    
#        return -1

# 2. brute force 
    def strStr(self, haystack, needle):
        lenHay, lenNeedle = len(haystack), len(needle)
        if lenHay < lenNeedle: return -1

        i = 0
        while i < lenHay - lenNeedle  + 1:
            j = 0
            while j < lenNeedle:
                if haystack[i + j] == needle[j]: j += 1
                else: break
            
            if j == lenNeedle: return i
            else: i += 1
        
        if i == lenHay - lenNeedle  + 1: return -1
        else: return i     
            
            
if __name__ == "__main__":
    test = Solution()
    haystack, needle = "", ""
    print test.strStr(haystack, needle)        
            
            
            