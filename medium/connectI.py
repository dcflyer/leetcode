# -*- coding: utf-8 -*-
"""
Given a binary tree

    struct TreeLinkNode {
      TreeLinkNode *left;
      TreeLinkNode *right;
      TreeLinkNode *next;
    }
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Note:

You may only use constant extra space.
You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).
For example,
Given the following perfect binary tree,
         1
       /  \
      2    3
     / \  / \
    4  5  6  7
After calling your function, the tree should look like:
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \  / \
    4->5->6->7 -> NULL
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
## 1. recurive method
#    def connect(self, root):
#        if not root: return
#        
#        if root.left:
#            root.left.next = root.right
#        if root.right:
#            root.right.next = root.next.left if root.next else None
#        self.connect(root.left)
#        self.connect(root.right)

# 2. iterative method, only keep the start of a list
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
                    
        
            
            
                        
        
        
        
