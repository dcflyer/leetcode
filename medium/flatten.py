# -*- coding: utf-8 -*-
"""
Given a binary tree, flatten it to a linked list in-place.

For example,
Given

         1
        / \
       2   5
      / \   \
     3   4   6
The flattened tree should look like:
   1
    \
     2
      \
       3
        \
         4
          \
           5
            \
             6
click to show hints.

Hints:
If you notice carefully in the flattened tree, 
each node's right child points to the next node of a pre-order traversal.

@author: Dennis
"""

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution:
    # @param root, a tree node
    # @return nothing, do it in place

## 1.recursive method
#    def flatten(self, root):
#        self.flattenHelp(root)
#        return
#            
#    def flattenHelp(self, root):
#        if not root: return root
#        
#        
#        left = self.flattenHelp(root.left)
#        right = self.flattenHelp(root.right)
#        
#        root.left = None
#        root.right = left
##        WRONG!!! left may be None, it.right may cause error
##        it = left
#        it = root
#        while it.right: it = it.right
#        it.right = right
#        
#        return root
        
# 2. iterative method
    def flatten(self, root):
        if not root: return
        
        stack = [root]
        prev = None
        
        while stack:
            curr = stack.pop()
            if curr.right: stack.append(curr.right)
            if curr.left: stack.append(curr.left)
            
            if prev:
                prev.left = None
                prev.right = curr
#                WRONG !!!
#                prev = curr
            prev = curr
        
        
if __name__ == "__main__":
    test = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    test.flatten(root)
        
        
        
        
        
        
        
        
        
        