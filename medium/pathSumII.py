# -*- coding: utf-8 -*-
"""
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
return
[
   [5,4,11,2],
   [5,8,4,5]
]

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
    # @param sum, an integer
    # @return a list of lists of integers
    def pathSum(self, root, sum):
        self.res = []
        if not root: return self.res
        path = []
        self.getPath(root, sum, path)                
        return self.res
    
#    def getPath(self, root, sum, path):
#        path.append(root.val)
#        
#        if not root.left and not root.right:
#            if root.val == sum:
#                self.res.append(path[:])
#        else:
#            if root.left:
#                self.getPath(root.left, sum - root.val, path)
#            if root.right:
#                self.getPath(root.right, sum - root.val, path)
#        
#        path.pop()

    def getPath(self, root, sum, path):
        path.append(root.val)
        
        if not root.left and not root.right:
            if root.val == sum:
                self.res.append(path[:])
#                WRONG !!!
#                path.pop()
            path.pop()
            return
            
        if root.left:
            self.getPath(root.left, sum - root.val, path)
        if root.right:
            self.getPath(root.right, sum - root.val, path)
        
        path.pop()     
#        
#    def getPath(self, root, sum, path):
#        
#        
#        if not root.left and not root.right:
#            if root.val == sum:
#                path.append(root.val)
#                self.res.append(path[:])
#                path.pop()
#            return
#            
#        path.append(root.val)    
#        if root.left:
#            self.getPath(root.left, sum - root.val, path)
#        if root.right:
#            self.getPath(root.right, sum - root.val, path)
#        path.pop()          
            
if __name__ == "__main__":
    test = Solution()
    
                
            
