# -*- coding: utf-8 -*-
"""
Given two words (start and end), and a dictionary, find the length of shortest transformation sequence from start to end, such that: 

1.Only one letter can be changed at a time
2.Each intermediate word must exist in the dictionary
For example, 

Given:
start = "hit"
end = "cog"
dict = ["hot","dot","dog","lot","log"]


As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5. 

Note:


Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.

@author: n609874
"""

class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return an integer
## 1. too slow, time limit exceeded
#    def ladderLength(self, start, end, dict):
#        if not start or not end or not dict: return 0
#        
#        queue = [start]
#        hashset = set([start])
#        level, curr, prev = 1, 0, 1
#        
#        while queue:
#            word = queue.pop(0)
#            prev -= 1
#            for i in xrange(len(word)):
#                for j in 'abcdefghijklmnopqrstuvwxyz':
#                    if j != word[i]:
#                        newword = word[:i] + j + word[i + 1:]
#                        if newword == end:
#                            return level + 1
#                        if newword in dict and newword not in hashset:
#                            hashset.add(newword)
#                            queue.append(newword)
#                            curr += 1
#            if 0 == prev:
#                prev, curr = curr, 0
#                level += 1
#        
#        return 0
    
    def ladderLength(self, start, end, dict):
        import collections
        wordLen = len(start)
        queue = collections.deque([(start, 1)])
        while queue:
            curr = queue.popleft()
            currWord = curr[0]; currLen = curr[1]
            if end == currWord: return currLen
            for i in xrange(wordLen):
                part1 = currWord[:i]; part2 = currWord[i + 1:]
                for j in 'abcdefghijklmnopqrstuvwxyz':
                    newWord = part1 + j + part2
                    if newWord in dict:
                        queue.append((newWord, currLen + 1))
                        dict.remove(newWord)
        return 0
        
if __name__ == "__main__":
    test = Solution()
    print test.ladderLength("hit", "cog", set(["hot","dot","dog","lot","log"]))
        
