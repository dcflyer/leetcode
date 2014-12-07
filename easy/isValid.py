# -*- coding: utf-8 -*-
"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

@author: n609874
"""
class Solution:
    # @return a boolean
    def isValid(self, s):
        table = []
        leftparen = ['(', "[", "{"]
        rightparen = [')', ']', '}']
        parentheses = dict(zip(rightparen, leftparen))

        for char in s:
            if char in leftparen:
                table.append(char)
                continue
            if char in parentheses:
                if table and table[-1] == parentheses[char]:
                    table.pop()
                else:
                    return False
#        WRONG!!! stack should be empty
#        return True
        return True if not table else False

if __name__ == "__main__":
    test = Solution()
    sList = ["()", "()[]{}", "(]", "([)]"]
    for s in sList:
        print s, test.isValid(s)