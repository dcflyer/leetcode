# -*- coding: utf-8 -*-
"""
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

For example, 

    1
   / \
  2   3

The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13. 
Return the sum = 12 + 13 = 25. 

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
    def sumNumbers(self, root):
        if not root: return 0
        return self.helper(0, root)
        
    def helper(self, res, root):
        if not root: return 0
        if not root.left and not root.right:
#            WRONG !!!
#            return root.val
            return res*10 + root.val
        return self.helper(10*res + root.val, root.left) + \
            self.helper(10*res + root.val, root.right)
            
if __name__ == "__main__":
    test = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    print test.sumNumbers(root)