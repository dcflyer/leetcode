# -*- coding: utf-8 -*-
"""
Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

Note:
A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?

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
    # @return a tree node
## 1. iterative way
#    def recoverTree(self, root):
#        if not root: return root
#        
#        prev, first, second = None, None, None
#        
#        stack, curr = [], root
#        while curr or stack:
#            if curr:
#                stack.append(curr)
#                curr = curr.left
#            else:
#                curr = stack.pop()
#                if prev and prev.val > curr.val:
#                    if not first:
#                        first, second = prev, curr
#                    else:
#                        second = curr
#                prev, curr = curr, curr.right
#        if first and second:
#            first.val, second.val = second.val, first.val
#        
#        return root
# 2. recursive way
    def recoverTree(self, root):
        if not root: return root
        
        self.prev = self.first = self.second = None
        self.helper(root)
        if self.first and self.second:
            self.first.val, self.second.val = self.second.val, self.first.val
        
        return root
    
    def helper(self, root):
        if not root: return
    
        self.helper(root.left)
        if self.prev and self.prev.val > root.val:
            if not self.first:
                self.first, self.second = self.prev, root
            else:
                self.second = root
                
#       WRONG !!! Don't miss this line
        self.prev = root
        self.helper(root.right)

    
if __name__ == "__main__":
    test = Solution()
    root = TreeNode(2)
    root.left = TreeNode(3)
    root.right = TreeNode(1)
    root = test.recoverTree(root)
    
    
                
        