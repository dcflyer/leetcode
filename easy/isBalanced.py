# -*- coding: utf-8 -*-
"""
Given a binary tree, determine if it is height-balanced. 

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1. 

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
    def isBalanced(self, root):
        if not root: return True
        
        if self.isBalanced(root.left) and \
            self.isBalanced(root.right) and \
            abs(self.height(root.left) - self.height(root.right)) < 2:
                return True
        else:
            return False
    
    def height(self, root):
        if not root: return 0
        
        return max(self.height(root.left), self.height(root.right)) + 1
        
if __name__ == "__main__":
    test = Solution()
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(4)
    
    print test.isBalanced(root)
        