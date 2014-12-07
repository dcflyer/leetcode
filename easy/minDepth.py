# -*- coding: utf-8 -*-
"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

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
    # @return an integer

##### WRONG, works for maxDepth, but not for minDepth
##### The minimum depth is the number of nodes along the shortest path from 
##### the root node down to the nearest leaf node.
#    def minDepth(self, root):
#        if not root: return 0
#        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1       

#    consider the one-sided tree case!!!!!!!!!!!!!
#    def minDepth(self, root):
#        if not root: return 0
#        
#        minleft = self.minDepth(root.left)
#        minright = self.minDepth(root.right)
#        
#        if not minleft: return minright + 1
#        if not minright: return minleft + 1
#        return min(minleft, minright) + 1

    def minDepth(self, root):
        if not root: return 0
        
        queue = [root, None]
        minDepth = 0
        while queue:
            curr = queue[0]
            del(queue[0])
            
            if curr:
                if curr.left: queue.append(curr.left)
                if curr.right: queue.append(curr.right)
                if not (curr.left or curr.right):
                    minDepth += 1
                    break
            else:
                minDepth += 1
                if queue: queue.append(None)
            
        return minDepth
                
if __name__ == "__main__":
    
    TreeList = []
    valList = list("ABCDEFGHI")
    
    for val in valList:
        TreeList.append(TreeNode(val))
           
    TreeList[valList.index('B')].left = TreeList[valList.index('A')]
    TreeList[valList.index('B')].right = TreeList[valList.index('D')]
    TreeList[valList.index('D')].left = TreeList[valList.index('C')]
    TreeList[valList.index('D')].right = TreeList[valList.index('E')]
    TreeList[valList.index('I')].left = TreeList[valList.index('H')]
    TreeList[valList.index('G')].right = TreeList[valList.index('I')]
    TreeList[valList.index('F')].left = TreeList[valList.index('B')]
    TreeList[valList.index('F')].right = TreeList[valList.index('G')]
    
    root = TreeList[valList.index('F')]
    
#    root = TreeNode('A')
#    leaf = TreeNode('B')
#    root.left = leaf
    
    test = Solution()
    print test.minDepth(root)