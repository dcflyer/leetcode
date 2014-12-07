# -*- coding: utf-8 -*-
"""
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

@author: Dennis
"""

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution:
    # @param num, a list of integers
    # @return a tree node
    def sortedArrayToBST(self, num):
        if not num or not len(num):
            return None
        return self.helper(num, 0, len(num) - 1)
        
    def helper(self, num, l, r):
        if l > r: return None
        
        m = (l + r)//2
        root = TreeNode(num[m])
        root.left = self.helper(num, l, m - 1)
        root.right = self.helper(num, m + 1, r)
        
        return root
    
    def inOrder(self, root):
        res = []
        if not root: return res
        
        stack = []
        curr = root
        while True:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                if not stack:
                    return res
                else:
                    curr = stack.pop()
                    res.append(curr.val)
                    curr = curr.right
   
if __name__ == "__main__":
    test = Solution()
    root = test.sortedArrayToBST([1,2,3,4,5])
    print test.inOrder(root)