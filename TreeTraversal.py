# -*- coding: utf-8 -*-
"""
Created on Fri Oct 31 15:39:02 2014

@author: n609874
"""
#class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None
#        self.visited = False

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

        
class Tree:
#    def inOrder(self, root):
#        stack = []
#        stack.append(root)
#        while stack:
#            top = stack[-1]
#            if top:
#                if top.visited:
#                    print top.val
#                    stack.pop()
#                    stack.append(top.right)
#                else:
#                    stack.append(top.left)
#            else:
#                stack.pop()
#                if stack:
#                    stack[-1].visited = True
    def inOrder(self, root):
        if not root: return
        
        stack = []
        current = root  # current will go over the whole tree
        while True:
            if current:
                stack.append(current)   # the only place to add node to stack
                current = current.left  # once add a node, add its left afterwards
            else:
                if not stack:
                    return
                else:
                    current = stack[-1]
                    stack.pop() # once touch node from stack, move current to right
                    print current.val
                    current = current.right
                    
    def preOrder(self, root):
        if not root: return
        
        stack = []
        stack.append(root)
        
        while stack:
            current = stack[-1]
            print current.val
            stack.pop()
            if current.right:
                stack.append(current.right)
#            WRONT!!!!!!!!!!!!  elif current.left:
            if current.left:
                stack.append(current.left)
    
#    def postOrder(self, root):
#        stack = []
#        stack.append(root)
#        prev = None
#        
#        while stack:
#            curr = stack[-1]
#            # we are traversing down the tree
#            if not prev or prev.left == curr or prev.right == curr:
#                if curr.left:
#                    stack.append(curr.left)
#                elif curr.right:
#                    stack.append(curr.right)
#                else:
#                    print curr.val
#                    stack.pop()
#            # we are traversing up the tree from the left
#            elif curr.left == prev:
#                if curr.right:
#                    stack.append(curr.right)
#                else:
#                    print curr.val
#                    stack.pop()
#            # we are traversing up the tree from the right
#            elif curr.right == prev:
#                print curr.val
#                stack.pop()
#            # record previously traversed node
#            prev = curr
            
    def postOrder(self, root):
        if not root: return
        
        stack = [root]
        prev = None
        
        while stack:
            curr = stack[-1]
            if not prev or prev.left == curr or prev.right == curr:
                if curr.left:
                    stack.append(curr.left)
                elif curr.right:
                    stack.append(curr.right)
            elif curr.left == prev:
                if curr.right:
                    stack.append(curr.right)
            else:
                print curr.val
                stack.pop()
            prev = curr
            
    def postOrderTwoStacks(self, root):
        # It is doing a reversed pre-order traversal. 
        # That is, the order of traversal is a node, 
        # then its right child followed by its left child. 
        if not root: return
            
        s1 = [root]
        s2 = []
        
        while s1:
            curr = s1[-1]
            s2.append(curr)
            s1.pop()
            if curr.left:
                s1.append(curr.left)
#            WRONG!!!! only have left node
#            elif curr.right:
            if curr.right:
                s1.append(curr.right)
            
        while s2:
            print s2[-1].val
            s2.pop()           
            
    
    def BFSTwoQueue(self, root):
        # with two queues
        if not root: return
        
        currqueue = [root]
        nextqueue = []
        
        while currqueue:
            curr = currqueue[0]
            del(currqueue[0])
            if curr:
                print curr.val
                nextqueue.append(curr.left)
                nextqueue.append(curr.right)
            if not currqueue:
                currqueue = nextqueue
                nextqueue = []
                
                
#    def BFSOneQueue(self, root):
#        # with only one queue
#        if not root: return
#        
#        queue = [root]
#        currnum = 1
#        nextnum = 0
#        
#        while queue:
#            curr = queue[0]
#            del(queue[0])
#            currnum -= 1
#            if curr:
#                print curr.val
#                queue.append(curr.left)
#                queue.append(curr.right)
#                nextnum += 2
#            if currnum == 0:
#                currnum = nextnum
#                nextnum = 0
    def BFSOneQueue(self, root):
        # use None to seperate levels
        if not root: return

        queue = [root]
        queue.append(None)
        level = 0
        
        while queue:
            curr = queue[0]
            del(queue[0])
            
            if curr:
                print curr.val
                if curr.left: queue.append(curr.left)
                if curr.right: queue.append(curr.right)
            else:
                level += 1
                if queue: queue.append(None)
                    
    
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
    test = Tree()
#    test.inOrder(root)
#    test.preOrder(root)
#    test.postOrder(root)
    test.BFSOneQueue(root)
#    test.BFSTwoQueue(root)
#    test.postOrderTwoStacks(root)