# -*- coding: utf-8 -*-
"""
Given n, generate all structurally unique BST's (binary search trees) that store values 1...n.

For example,
Given n = 3, your program should return all 5 unique BST's shown below. 

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3


@author: n609874
"""

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @return a list of tree node
    def generateTrees(self, n):
        return self.generate(1, n)
    
    def generate(self, left, right):
        
        if left > right:
            return [None]
        if left == right:
            [TreeNode(left)]
        res = []
        for k in xrange(left, right + 1):
            leftList = self.generate(left, k - 1)
            rightList = self.generate(k + 1, right)
            for i in leftList:
                for j in rightList:
                    root = TreeNode(k)
                    root.left = i
                    root.right = j
                    res.append(root)
        
        return res           
                
if __name__ == "__main__":
    test = Solution()
    test.generateTrees(3)
    
        
