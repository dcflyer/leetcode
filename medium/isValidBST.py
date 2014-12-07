# -*- coding: utf-8 -*-
"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

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
    # @return a boolean
## 1. recursive method
#    def isValidBST(self, root):      
#        return self.isValidSub(root, -2147483648, 2147483647)
#
###   WRONG !!! when root contains max (2147483647) or min (-2147483648), fails
###   not a good idea to check root.val with <= or >=
##    def isValidSub(self, root, minV, maxV):
##        if not root: return True
###       WRONG !!! consider non distinct values                                
###        if root.val > maxV or root.val < minV:
##        if root.val >= maxV or root.val <= minV:
##            return False
##        return self.isValidSub(root.left, minV, root.val) and \
##                self.isValidSub(root.right, root.val, maxV)
#
#    def isValidSub(self, root, minV, maxV):
#        if not root: return True
#        if root.val > maxV or root.val < minV:
#            return False
#        return self.isValidSub(root.left, minV, root.val - 1) and \
#                self.isValidSub(root.right, root.val + 1, maxV)
                
    def isValidBST(self, root):
        res = self.inorderTraversal(root)
        if len(res) > 1:
            for i in xrange(1, len(res)):
                if res[i] <= res[i - 1]:
                    return False
        return True
        
    def inorderTraversal(self, root):
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
    root = TreeNode(1)
    root.right = TreeNode(1)
    print test.isValidBST(root)
        