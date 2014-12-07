# -*- coding: utf-8 -*-
"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

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

#    def maxDepth(self, root):
#        if root == None: return 0
#        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
    
#    # use postOrder DFS
#    def maxDepth(self, root):
#        if not root: return 0
#        stack = []
#        stack.append(root)
#        prev = None
#        maxDepth = 0
#        
#        while stack:
#            curr = stack[-1]
#            if not prev or prev.left == curr or     def maxDepth(self, root):
#        if not root: return 0
#        
#        queue = [root]
#        queue.append(None)
#        maxDepth = 0
#
#        while queue:
#            curr = queue[0]
#            del(queue[0])
#            
#            if curr:
#                if curr.left: queue.append(curr.left)
#                if curr.right: queue.append(curr.right)
#            else:
#                maxDepth += 1
#                if queue: queue.append(None)
#        
#        return maxDepthprev.right == curr:
#                if curr.left:
#                    stack.append(curr.left)
#                elif curr.right:
#                    stack.append(curr.right)
#            elif curr.left == prev:
#                if curr.right:
#                    stack.append(curr.right)
#            else:
##                print curr.val
#                stack.pop()
#            prev = curr
#            
#            if len(stack) > maxDepth:
#                maxDepth = len(stack)
#        return maxDepth
    
    def maxDepth(self, root):
        if not root: return 0
        
        queue = [root]
        queue.append(None)
        maxDepth = 0

        while queue:
            curr = queue[0]
            del(queue[0])
            
            if curr:
                if curr.left: queue.append(curr.left)
                if curr.right: queue.append(curr.right)
            else:
                maxDepth += 1
                if queue: queue.append(None)
        
        return maxDepth
                

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
    test = Solution()
    
    print test.maxDepth(root)