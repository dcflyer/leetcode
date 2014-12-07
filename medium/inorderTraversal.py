# -*- coding: utf-8 -*-
"""
Given a binary tree, return the inorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},


   1
    \
     2
    /
   3

return [1,3,2]. 

Note: Recursive solution is trivial, could you do it iteratively?

@author: n609874
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
#    def inorderTraversal(self, root):
#        if not root: return[]
#
#        stack = []
#        res = []
#        curr = root
#        while True:
#            if curr:
#                stack.append(curr)
#                curr = curr.left
#            else:
#                if not stack:
#                    return res
#                else:
#                    curr = stack.pop()
#                    res.append(curr.val)
#                    curr = curr.right
                    
    def inorderTraversal(self, root):
        res, stack = [], []
        if not root: return res
        
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                res.append(root.val)
                root = root.right
        
        return res
                    
if __name__ == "__main__":
    test = Solution()
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    print test.inorderTraversal(root)
