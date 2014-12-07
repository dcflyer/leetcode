# -*- coding: utf-8 -*-
"""
Given a binary tree, return the preorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},

   1
    \
     2
    /
   3

return [1,2,3].

Note: Recursive solution is trivial, could you do it iteratively?
@author: weichen
"""

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers

## 1. leetcode method
#    def preorderTraversal(self, root):
#        if not root: return []
#        stack = [root]
#        res = []
#        while stack:
#            top = stack.pop()
#            res.append(top.val)
#            if top.right: stack.append(top.right)
#            if top.left: stack.append(top.left)  
#        return res

    def preorderTraversal(self, root):     
        res, stack = [], []
        if not root: return res        
        
        while root or stack:
            if root:
                res.append(root.val)
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                root = root.right
        
        return res
        
if __name__ == "__main__":
    test = Solution()
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    print test.preorderTraversal(root)
    
