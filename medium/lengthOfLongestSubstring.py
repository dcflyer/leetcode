# -*- coding: utf-8 -*-
"""
Given a string, find the length of the longest substring without repeating characters. 
For example, the longest substring without repeating letters for "abcabcbb" is "abc", 
which the length is 3. For "bbbbb" the longest substring is "b", with the length of 1.

@author: weichen
"""
class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        pos = {}
        last = -1
        maxlen = 0
        
        for i in xrange(len(s)):
            if s[i] in pos and last < pos[s[i]]:
                last = pos[s[i]]
            if i - last > maxlen:
                maxlen = i - last
            pos[s[i]] = i
        
        return maxlen
            
        

if __name__ == "__main__":
    test = Solution()
    strList = ["abcabcbb", "bbbbb"]
    for s in strList:
        print test.lengthOfLongestSubstring(s)