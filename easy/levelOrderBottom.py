# -*- coding: utf-8 -*-
"""
Created on Fri Nov  7 09:05:17 2014

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
    def levelOrderBottom(self, root):
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
                res.insert(0, level[:])
                level = []
                if queue: queue.append(None)

        return res
if __name__ == "__main__":
    test = Solution()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)                
    root.right.right = TreeNode(7)

    print test.levelOrderBottom(root)              
