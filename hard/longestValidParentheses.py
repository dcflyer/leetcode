# -*- coding: utf-8 -*-
"""
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

For "(()", the longest valid parentheses substring is "()", which has length = 2.

Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.

@author: Dennis
"""

class Solution:
    # @param s, a string
    # @return an integer
# WRONG !!! doesn't work on ")(", stack = [-1] has a problem
# when you use s[stack[-1]], insert a dummy element should insert
# both index and char
#    def longestValidParentheses(self, s):
#        res = 0
#        if not s: return res
#        stack = [-1]
#        for i in xrange(len(s)):
#            if ')' == s[i] and '(' == s[stack[-1]]:
#                stack.pop()
#                res = max(res, i - stack[-1])
#            else:
#                stack.append(i)
#        return res

## 1. insert dummy element
#    def longestValidParentheses(self, s):
#        res = 0
#        stack = [(-1, ')')]
#        for i, c in enumerate(s):
#            if ')' == c and '(' == stack[-1][1]:
#                stack.pop()
#                res = max(res, i - stack[-1][0])
#            else:
#                stack.append([i, c])
#        return res
# 2. no dummy element
    def longestValidParentheses(self, s):
        res = 0
        if not s: return res
        stack = []
        for i in xrange(len(s)):
            if ')' == s[i] and stack and '(' == s[stack[-1]]:
                stack.pop()
                if not stack:
                    res = i + 1
                else:
                    res = max(res, i - stack[-1])
            else:
                stack.append(i)
                
        return res        

if __name__ == "__main__":
    test = Solution()
    print test.longestValidParentheses(")()())")
    print test.longestValidParentheses(")(")
