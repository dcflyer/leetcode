# -*- coding: utf-8 -*-
"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses. 

For example, given n = 3, a solution set is: 

"((()))", "(()())", "(())()", "()(())", "()()()" 

@author: n609874
"""

class Solution:
    # @param an integer
    # @return a list of string

# Catalan number: C_0 = 1, C_{n + 1} = \sum_{i = 0}^n C_i C_{n - i}
# 这个题对于C的定义就是第一对括号中包含有几组括号。
# C_0 = 1:                                           empty
# C_1 = C_0 C_0 = 1:                                 ()
# C_2 = C_1 C_0 + C_0 C_1 = 1 + 1 = 2:               (()), ()()
# C_3 = C_2 C_0 + C_1 C_1 + C_0 C_2 = 2 + 1 + 2 = 5: ((())), (()()), (())(), ()(()), ()()() 

    def generateParenthesis(self, n):
        self.res = []
        if n <= 0: return self.res
        self.helper("", n, n)
        return self.res

    def helper(self, combination, l, r):
        if l > r: return        
        if 0 == l and 0 == r: 
            self.res.append(combination)
            return
        if l > 0: self.helper(combination + "(", l - 1, r)
        if r > 0: self.helper(combination + ")", l, r - 1)
            
if __name__ == "__main__":
    test = Solution()
    print test.generateParenthesis(3)