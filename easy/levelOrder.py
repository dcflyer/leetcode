# -*- coding: utf-8 -*-
"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7

return its level order traversal as:


[
  [3],
  [9,20],
  [15,7]
]

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
    # @return a list of lists of integers
#    def levelOrder(self, root):
#        res = []
#        if not root: return res
#         
#        curr = [root]
#        next = []
#        level = []
#        
#        while curr:
#            front = curr[0]
#            level.append(front.val)
##            #### WILL CHANGE the list of lists ####
#            del(curr[0]) ######
#            if front.left: next.append(front.left)            
#            if front.right: next.append(front.right)
#            if not curr:
#                res.append(level[:]) # use deep copy
#                level = []
#                curr = next
#                next = []
#        return res
#
#    def levelOrder(self, root):
#        if not root: return []        
#        
#        queue = [root]
#        currlevel = 1
#        nextlevel = 0
#        res = []
#        level = []
#        
#        while queue:
#            front = queue.pop(0)
#            level.append(front.val)
#            currlevel -= 1
#            if front.left:
#                queue.append(front.left)
#                nextlevel += 1
#            if front.right:
#                queue.append(front.right)
#                nextlevel += 1
#            if not currlevel:
#                res.append(level[:])
#                level = []
#                currlevel = nextlevel
#                nextlevel = 0
#        return res
    def levelOrder(self, root):
        res = []
        if not root: return res
    
        queue = [root, None]
        level = []

        while queue:
            front = queue.pop(0)
            if front:
                level.append(front.val)
                if front.left: queue.append(front.left)                
                if front.right: queue.append(front.right)  
            else:
                res.append(level[:])
                level = []
#                Don't miss this line !!!!!!!!!!
                if queue:
                    queue.append(None)
        return res

if __name__ == "__main__":
    test = Solution()
    root = TreeNode(1)
#    root.right = TreeNode(2)
    res = test.levelOrder(root)
            
        
        
        





















