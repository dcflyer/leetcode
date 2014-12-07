# -*- coding: utf-8 -*-
"""
Follow up for problem "Populating Next Right Pointers in Each Node".

What if the given tree could be any binary tree? Would your previous solution still work?

Note:

You may only use constant extra space.
For example,
Given the following binary tree,
         1
       /  \
      2    3
     / \    \
    4   5    7
After calling your function, the tree should look like:
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \    \
    4-> 5 -> 7 -> NULL
    
@author: Dennis
"""

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        if not root: return
        
        prevList, currList = root, None
        prevIter, currIter = prevList, currList
        while prevIter:
            if prevIter.left:
                if currIter:
                    currIter.next = prevIter.left
                    currIter = currIter.next
                else:
                    currList = prevIter.left
                    currIter = currList
            if prevIter.right:
                if currIter:
                    currIter.next = prevIter.right
                    currIter = currIter.next
                else:
                    currList = prevIter.right
                    currIter = currList
            prevIter = prevIter.next
            
            if not prevIter:
                if currList:
                    prevList, currList = currList, None
                    prevIter, currIter = prevList, currList
        
        return
        
        