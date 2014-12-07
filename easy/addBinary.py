# -*- coding: utf-8 -*-
"""
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100". 

@author: weichen
"""

class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        l_a = len(a); l_b = len(b)
        if l_a >= l_b:
            b = "0"*(l_a - l_b) + b
        else:
            a = "0"*(l_b - l_a) + a
        
        res = ""; carry = 0
        

        # not reverse a, b
        for i in xrange(len(a)-1, -1, -1):
            ai = 0 if a[i] == "0" else 1
            bi = 0 if b[i] == "0" else 1
#            CHANGE RES FIRST, O.W. carry changed before added to res
            res = str((ai + bi + carry)%2) + res
            carry = (ai + bi + carry)/2
        if carry == 1: res = "1" + res

#        # reverse a, b
#        a = a[::-1]; b = b[::-1]
#        for i in xrange(len(a)):
#            ai = 0 if a[i] == "0" else 1
#            bi = 0 if b[i] == "0" else 1
#            res += str((ai + bi + carry)%2)
#            carry = (ai + bi + carry)/2            
#        if carry == 1: res += "1"            
            
        return res
        
if __name__ == "__main__":
    test = Solution()
    t = [("1", "1"), ("1011", "0"), ("10", "10111")]
    for e in t:
        print test.addBinary(e[0], e[1])
    
        
