# -*- coding: utf-8 -*-
"""
Given a binary tree, return the postorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},

   1
    \
     2
    /
   3

return [3,2,1].

Note: Recursive solution is trivial, could you do it iteratively?
@author: weichen
"""

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers

## 1. leetcode method
#    def postorderTraversal(self, root):
#        res = []
#        if not root: return res
#        prev = None
#        stack = [root]
#        
#        
#        while stack:
#            curr = stack[-1]
#            if not prev or prev.left == curr or prev.right == curr:
#                if curr.left: 
#                    stack.append(curr.left)
#                elif curr.right:
#                    stack.append(curr.right)
#            elif curr.left == prev:
#                if curr.right:
#                    stack.append(curr.right)
#            else:
#                res.append(curr.val)
#                stack.pop()
#            prev = curr
#        
#        return res

    def postorderTraversal(self, root):
        res, stack = [], []
        if not root: return res

        prev = None
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            elif stack[-1].right != prev:
                root = stack[-1].right
                prev = None
            else:
                prev = stack.pop()
                res.append(prev.val)
        return res
            
            
if __name__ == "__main__":
    test = Solution()
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    print test.postorderTraversal(root)
        
        
        
        
        
        
        
        
        
        