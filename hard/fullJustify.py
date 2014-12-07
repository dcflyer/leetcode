# -*- coding: utf-8 -*-
"""
Given an array of words and a length L, format the text such that each line has exactly L characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly L characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

For example,
words: ["This", "is", "an", "example", "of", "text", "justification."]
L: 16.

Return the formatted lines as:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
Note: Each word is guaranteed not to exceed L in length.

@author: Dennis
"""

class Solution:
    # @param words, a list of strings
    # @param L, an integer
    # @return a list of strings
    def fullJustify(self, words, L):
        res = []
        count, start = 0, 0

        for i in xrange(len(words)):
            if count + len(words[i]) + i - start > L: # fail to add the ith word
                withinspace, extraspace = 0, 0
                if i - start - 1 > 0:
                    withinspace = (L - count)/(i - start - 1)
                    extraspace = (L - count)%(i - start - 1)
                line = ""
                for j in xrange(start, i - 1):  # only add up to i-1 th word
                    line += words[j] + " "*withinspace
                    if extraspace > 0:
                        line += " "; extraspace -= 1
                line += words[i - 1]
                
#                for the case when there is only one word in the line
                line += " "*(L - len(line))
                
                res.append(line)
                count, start = 0, i
#            else:
#                count += len(words[i])
            count += len(words[i])
        
#        deal with the last line
        line = ""
        for i in xrange(start, len(words)):
            line += words[i]
            if len(line) < L: line += " "
        
        line += " "*(L - len(line))
        res.append(line)
        
        return res
        
if __name__ == "__main__":
    test = Solution()
#    L, words = 16, ["This", "is", "an", "example", "of", "text", "justification."]
#    L, words = 3, ["a","b","c","d","e"]
    L, words = 12, ["What","must","be","shall","be."]
    print test.fullJustify(words, L)
        
        