# -*- coding: utf-8 -*-
"""
Given a binary tree, find the maximum path sum. 

The path may start and end at any node in the tree. 

For example:
Given the below binary tree, 

       1
      / \
     2   3

Return 6. 

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
    # @return an integer
    def maxPathSum(self, root):
        if not root: return 0
        self.res = root.val
        self.helper(root)
        return self.res
        
    def helper(self, root):
        if not root: return 0
        
        left = self.helper(root.left)
        right = self.helper(root.right)
#        WRONG !!! consider left and right to be negative
#        rootsum = left + right + root.val
        rootsum = max(left, 0) + max(right, 0) + root.val
        self.res = max(self.res, rootsum)
#        WRONG !!! consider left and right to be negative
#        return root.val + (left if left > right else right)
        return root.val + max(max(left, right), 0)
    
if __name__ == "__main__":
    test = Solution()
    root = TreeNode(-1)
    root.left = TreeNode(-22)
    root.right = TreeNode(-3)
    print test.maxPathSum(root)    
        
        
        