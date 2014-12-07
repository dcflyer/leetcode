# -*- coding: utf-8 -*-
"""
Given an array of strings, return all groups of strings that are anagrams. 

Note: All inputs will be in lower-case.

@author: n609874
"""

class Solution:
    # @param strs, a list of strings
    # @return a list of strings
    def anagrams(self, strs):
        res = []
        if not strs: return res
        
        hashmap = {}
        for x in strs:
            key = ''.join(sorted(x))
            if key in hashmap:
                hashmap[key].append(x)
            else:
                value = [x]
                hashmap[key] = value
        
        for key, value in hashmap.items():
            if len(value) > 1:
                res += value
        return res

if __name__ == "__main__":
    test = Solution()
    strs = [ "abc", "efg", "cba" , "feg" ]
    print test.anagrams(strs)
    
        