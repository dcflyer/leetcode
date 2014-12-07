# -*- coding: utf-8 -*-
"""
Given two words (start and end), and a dictionary, find all shortest transformation sequence(s) from start to end, such that: 

1.Only one letter can be changed at a time
2.Each intermediate word must exist in the dictionary
For example, 

Given:
start = "hit"
end = "cog"
dict = ["hot","dot","dog","lot","log"]


Return


  [
    ["hit","hot","dot","dog","cog"],
    ["hit","hot","lot","log","cog"]
  ]

Note:


All words have the same length.
All words contain only lowercase alphabetic characters.

@author: n609874
"""

class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return a list of lists of string
    def findLadders(self, start, end, dict):
        self.res = []
        self.prevmap = {}
        for word in dict:
            self.prevmap[word] = []
        
        candidates = [set(), set()]
        curr, prev = 0, 1
        candidates[curr].add(start)
        
        while True:
            curr, prev = prev, curr
            candidates[curr].clear()
            for word in candidates[prev]:
                dict.remove(word)
            for word in candidates[prev]:
                for i in xrange(len(word)):
                    for j in 'abcdefghijklmnopqrstuvwxyz':
                        if j != word[i]:
                            newword = word[:i] + j + word[i + 1:]
                            if newword in dict:
                                candidates[curr].add(newword)
#                                WRONG !!!
#                                self.prevmap[word].append(newword)                                
                                self.prevmap[newword].append(word)
            if 0 == len(candidates[curr]): return self.res
            if end in candidates[curr]: break
    
        self.buildpath([], end)
        return self.res
        
    def buildpath(self, path, word):
        path.append(word)
        if 0 == len(self.prevmap[word]):
            currpath = path[:]
            currpath.reverse()
            self.res.append(currpath)
        else:
            for prevword in self.prevmap[word]:
                self.buildpath(path, prevword)
        path.pop()
        
if __name__ == "__main__":
    test = Solution()
    print test.findLadders("hit", "cog", set(["hit", "hot","dot","dog","lot","log", "cog"]))        
        