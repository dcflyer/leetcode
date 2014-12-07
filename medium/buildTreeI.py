# -*- coding: utf-8 -*-
"""
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

@author: Dennis
"""

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param preorder, a list of integers
    # @param inorder, a list of integers
    # @return a tree node
## 1. traditional way, not good enough for Python
#    def buildTree(self, preorder, inorder):
#        if not preorder or not inorder: return None
#        
#        hashmap = {}
#        for i in xrange(len(inorder)):
#            hashmap[inorder[i]] = i
#        
#        return self.helper(preorder, 0, len(preorder) - 1, \
#            inorder, 0, len(inorder) - 1, hashmap)
#        
#    def helper(self, preorder, preS, preE, \
#            inorder, inS, inE, hashmap):
#        
#        if preS > preE or inS > inE: return None
#        
#        root = TreeNode(preorder[preS])
#        index = hashmap[preorder[preS]]
#        root.left = self.helper(preorder, preS + 1, index - inS + preS, \
#                    inorder, inS, index - 1, hashmap)
#        root.right = self.helper(preorder, index - inS + preS + 1, preE, \
#                    inorder, index + 1, inE, hashmap)
#                    
#        return root
# 2. clean way 
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder: return None
        
        root = TreeNode(preorder[0])
        index = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:index + 1], inorder[:index])
        root.right = self.buildTree(preorder[index + 1:], inorder[index + 1:])
        return root
        
if __name__ == "__main__":
    test = Solution()
    root = test.buildTree(list("12453687"), list("42516837"))
    
        