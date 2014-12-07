# -*- coding: utf-8 -*-
"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases. 

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome. 

Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome. 

@author: n609874
"""
class Solution:
    # @param s, a string
    # @return a boolean
#    def isPalindrome(self, s):
#        UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#        LOWER = "abcdefghijklmnopqrstuvwxyz"
#        
#        trimed = ""
#        for c in s:
#            if c in UPPER or c in LOWER:
#                if c in UPPER: c = c.lower()
#                trimed += c

#    def isPalindrome(self, s):
#        left = 0; right = len(s) - 1
#        while left <= right:
#            if s[left].isalnum() and s[right].isalnum():
#                if s[left] != s[right]:
#                    return False
#                else:
#                    left += 1; right -= 1
#            elif s[left].isalnum():
#                right -= 1
#            else:
#                left +=1
#        return True

    def isPalindrome(self, s):
        left = 0; right = len(s) - 1
        while left <= right:
            if s[left].isalnum() and s[right].isalnum():
#                WRONG!!! if s[left] != s[right]:
                if s[left].lower() != s[right].lower():
                    return False
                left += 1; right -= 1
            else:
                if not s[left].isalnum():
                    left += 1
                if not s[right].isalnum():
                    right -= 1
        return True
        


if __name__ == "__main__":
    test = Solution()
    strs = ["A man, a plan, a canal: Panama", "race a car"]
    for s in strs:
        print s,test.isPalindrome(s)
        
        
        
        
