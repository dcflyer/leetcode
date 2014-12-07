# -*- coding: utf-8 -*-
"""
Given a digit string, return all possible letter combinations that the number could represent. 

A mapping of digit to letters (just like on the telephone buttons) is given below.



Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:
Although the above answer is in lexicographical order, your answer could be in any order you want. 

@author: n609874
"""

class Solution:
    # @return a list of strings, [s1, s2]
## 1. recursive way
#    def letterCombinations(self, digits):
#        if not digits: return [""]
#        
#        self.res = []
#        digits.replace('1', '')
#        self.phone = { 2:"abc", 3:"def", 4:"ghi", 5:"jkl", 6:"mno", 7:"pqrs", 8:"tuv", 9:"wxyz"}
#        self.helper("", digits)
#        return self.res
#
#    def helper(self, letter, digits):
#        if not digits:
#            self.res.append(letter)
#        else:
#            for char in self.phone[int(digits[0])]:
#                self.helper(letter + char, digits[1:])

# 2. iterative way
    def letterCombinations(self, digits):
        if not digits: return [""]

        digits.replace('1', '')
        self.phone = { 2:"abc", 3:"def", 4:"ghi", 5:"jkl", 6:"mno", 7:"pqrs", 8:"tuv", 9:"wxyz"}
        
        currLevel, nextLevel = [""], []
        for num in digits:
            for char in self.phone[int(num)]:
                for elem in currLevel:
                    nextLevel.append(elem + char)
            currLevel, nextLevel = nextLevel, []
        
        return currLevel
    
if __name__ == "__main__":
    test = Solution()
    print test.letterCombinations("23")