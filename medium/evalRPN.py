# -*- coding: utf-8 -*-
"""
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Some examples:
  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
  
@author: Dennis
"""

class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        if not tokens: return -1
        
        stack = []
        for x in tokens:
            if x not in ("+", "-", "*", "/"):
                stack.append(int(x))
            elif len(stack) < 2:
                return -1
            else:
                op2 = stack.pop()
                op1 = stack.pop()
                if "+" == x:
                    stack.append(op1 + op2)
                elif "-" == x:
                    stack.append(op1 - op2)
                elif "*" == x:
                    stack.append(op1 * op2)
                else:
                    stack.append(int(op1 * 1. / op2))
        if len(stack) > 1:
            return -1
        else:
            return stack[0]
            
if __name__ == "__main__":
    test = Solution()
    print test.evalRPN(["2", "1", "+", "3", "*"])
    print test.evalRPN(["4", "13", "5", "/", "+"])                    
                        
        