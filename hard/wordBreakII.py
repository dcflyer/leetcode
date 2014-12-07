# -*- coding: utf-8 -*-
"""
Given a string s and a dictionary of words dict, add spaces in s to construct a sentence where each word is a valid dictionary word. 

Return all such possible sentences. 

For example, given
s = "catsanddog",
dict = ["cat", "cats", "and", "sand", "dog"]. 

A solution is ["cats and dog", "cat sand dog"].

@author: n609874
"""
class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a list of strings
    def wordBreak(self, s, dict):
        self.res = []
        self.currBreak(s, dict, "")
        return self.res
#        
#    def currBreak(self, sub, dict, item):
#        if not sub:
#            self.res.append(item[:])
#        
#        for i in xrange(1, len(sub) + 1):
#            if sub[:i] in dict:
#                new_item = item + " " + sub[:i] if item else sub[:i]
#                self.currBreak(sub[i:], dict, new_item)

    def currBreak(self, sub, dict, item):
        if not self.checkBreak(sub, dict): return
        
        if not sub:
            self.res.append(item[:])
        
        for i in xrange(1, len(sub) + 1):
            if sub[:i] in dict:
                new_item = item + " " + sub[:i] if item else sub[:i]
                self.currBreak(sub[i:], dict, new_item)
    
    def checkBreak(self, sub, dict):
#        WRONG!!!!! can omit this one, or change it to return True
#        if not sub: return False
        check = [False for x in xrange(len(sub) + 1)]
        check[0] = True
        
        for i in xrange(1, len(sub) + 1):
            for j in xrange(i):
                if check[j] and sub[j:i] in dict:
                    check[i] = True
                    break;
        return check[-1]
        
        
if __name__ == "__main__":
    test = Solution()
    s = "catsanddog"
    dict = ["cat", "cats", "and", "sand", "dog"]
    print test.wordBreak(s, dict)
            
            