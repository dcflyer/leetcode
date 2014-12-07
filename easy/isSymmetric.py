# -*- coding: utf-8 -*-
"""
Created on Fri Nov  7 09:30:18 2014
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree is symmetric: 

    1
   / \
  2   2
 / \ / \
3  4 4  3

But the following is not:

    1
   / \
  2   2
   \   \
   3    3

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
    # @return a boolean
    def isSymmetric(self, root):
        if not root: return True
        
        return self.isSym(root.left, root.right)
        
    def isSym(self, r1, r2):
        if not r1 and not r2:
            return True
        elif not r1 or not r2:
            return False
        else:
            return r1.val == r2.val and \
                    self.isSym(r1.left, r2.right) and \
                    self.isSym(r1.right, r2.left)
if __name__ == "__main__":
    test = Solution()
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(4)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(3)
    
    print test.isSymmetric(root)
                
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
