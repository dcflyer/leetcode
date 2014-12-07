# -*- coding: utf-8 -*-
"""
The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ... 

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.


Given an integer n, generate the nth sequence. 

Note: The sequence of integers will be represented as a string. 

@author: n609874
"""
class Solution:
    # @return a string
    def countAndSay(self, n):
        s = "1"
        for i in xrange(1,n):
            s2 = ""
            count = 1
            for j in xrange(len(s)):
                if j != len(s) - 1 and s[j] == s[j+1]:
                    count += 1
                else:
                    s2 += str(count) + s[j]
                    count = 1
            s = s2
        return str(s)


if __name__ == "__main__":
    test = Solution()
    print test.countAndSay(2)
