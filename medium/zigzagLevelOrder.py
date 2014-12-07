# -*- coding: utf-8 -*-
"""
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
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
    # @return a list of lists of integers

## 1 . use queue 
#    def zigzagLevelOrder(self, root):
#        res = []
#        if not root: return res
#        
#        queue, level = [root, None], []
#        rev = False
#        while queue:
#            front = queue.pop(0)
#            if front:
#                if rev:
#                    level.insert(0, front.val)
#                else:
#                    level.append(front.val)
#                if front.left: queue.append(front.left)
#                if front.right: queue.append(front.right)
#            else:
#                res.append(level[:])
#                level = []
#                rev = not rev
##                Don't miss this line !!!!!!!!!!
#                if queue:                
#                    queue.append(None)
#        return res
        
# 2. use two stacks
    def zigzagLevelOrder(self, root):
        res = []
        if not root: return res
        
        stack, newstack, level = [root], [], []
        res = []
        rev = True
        while stack:
            
            while stack:
                curr = stack.pop()
                level.append(curr.val)
                if rev:
                    if curr.left: newstack.append(curr.left)
                    if curr.right: newstack.append(curr.right)
                else:
                    if curr.right: newstack.append(curr.right)
                    if curr.left: newstack.append(curr.left)
            
            res.append(level[:])
            level = []
            rev = not rev
            stack = newstack
            newstack = []
        return res

if __name__ == "__main__":
    test = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    print test.zigzagLevelOrder(root)


