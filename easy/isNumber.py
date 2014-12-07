# -*- coding: utf-8 -*-
"""
Validate if a given string is numeric.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true

0初始无输入或者只有space的状态
1输入了数字之后的状态
2前面无数字，只输入了dot的状态
3输入了符号状态
4前面有数字和有dot的状态
5'e' or 'E'输入后的状态
6输入e之后输入Sign的状态
7输入e后输入数字的状态
8前面有有效数输入之后，输入space的状态

Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one. 

###### Finite automata machine ######

@author: n609874
"""
class Solution:
    # @param s, a string
    # @return a boolean
    def isNumber(self, s):     
        import string
        INVALID=0; SPACE=1; SIGN=2; DIGIT=3; DOT=4; EXPONENT=5;
        #0invalid,1space,2sign,3digit,4dot,5exponent,6num_inputs
        transitionTable=[[-1,  0,  3,  1,  2, -1],    #0 no input or just spaces 
                         [-1,  8, -1,  1,  4,  5],    #1 input is digits 
                         [-1, -1, -1,  4, -1, -1],    #2 no digits in front just Dot 
                         [-1, -1, -1,  1,  2, -1],    #3 sign 
                         [-1,  8, -1,  4, -1,  5],    #4 digits and dot in front 
                         [-1, -1,  6,  7, -1, -1],    #5 input 'e' or 'E' 
                         [-1, -1, -1,  7, -1, -1],    #6 after 'e' input sign 
                         [-1,  8, -1,  7, -1, -1],    #7 after 'e' input digits 
                         [-1,  8, -1, -1, -1, -1]]    #8 after valid input input space

        
        state = 0; i = 0
        while i < len(s):
            inputchar = INVALID
            if s[i] == " ": inputchar = SPACE
            elif s[i] == "+" or s[i] == "-": inputchar = SIGN
            elif s[i] in string.digits: inputchar = DIGIT
            elif s[i] == ".": inputchar = DOT
            elif s[i] == "e" or s[i] == "E": inputchar = EXPONENT
        
            state = transitionTable[state][inputchar]
            if state == -1: return False
            else: i += 1
        
        return state == 1 or state == 4 or state == 7 or state == 8

if __name__ == "__main__":
    test = Solution()    
    strs = ["  2", "e", "3.4e", "4.5E5.6", "-1e+2 ", "+09.2E3 "]
    for s in strs:
        print s, test.isNumber(s)
        