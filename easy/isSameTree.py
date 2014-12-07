# -*- coding: utf-8 -*-
"""

Given two binary trees, write a function to check if they are equal or not. 

Two binary trees are considered equal if they are structurally identical and the nodes have the same value. 

@author: n609874
"""
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param p, a tree node
    # @param q, a tree node
    # @return a boolean
    def isSameTree(self, p, q):
        if not p and not q: return True
        if not p or not q: return False

        return p.val == q.val and \
            self.isSameTree(p.left, q.left) and \
            self.isSameTree(p.right, q.right)

if __name__ == "__main__":
    test = Solution()
    Tree1 = TreeNode(2)
    Tree1.left = TreeNode(3)
    
    Tree2 = TreeNode(2)
    Tree2.right = TreeNode(3)
    
    print test.isSameTree(Tree1, Tree2)