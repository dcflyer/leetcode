# -*- coding: utf-8 -*-
"""
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum. 

For example:
Given the below binary tree and sum = 22, 
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1

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
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):
        if not root: 
            return False        
        if not root.left and not root.right:
            return root.val == sum
        
        return self.hasPathSum(root.left, sum - root.val) or \
                self.hasPathSum(root.right, sum - root.val)
                     
if __name__ == "__main__":
    
    TreeList = []
    valList = [-2,-3]
    
    for val in valList:
        TreeList.append(TreeNode(val))          
    TreeList[valList.index(-2)].right = TreeList[valList.index(-3)]
    
    root = TreeList[valList.index(-2)]
    test = Solution()
    print test.hasPathSum(root, -5)
        