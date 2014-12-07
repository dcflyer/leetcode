# -*- coding: utf-8 -*-
"""
Given a singly linked list where elements are sorted in ascending order, 
convert it to a height balanced BST.

@author: Dennis
"""

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
class Solution:
    # @param head, a list node
    # @return a tree node
    def sortedListToBST(self, head):
        if not head: return head
        
        length, curr = 0, head
        while curr:
            curr = curr.next
            length += 1

        curr = [head]
        return self.helper(curr, 0, length - 1)
    
    def helper(self, curr, l, r):
        if l > r: return None
        
        m = (l + r)//2
        left = self.helper(curr, l, m - 1)
        root = TreeNode(curr[0].val)
        curr[0] = curr[0].next
        right = self.helper(curr, m + 1, r)
        root.left, root.right = left, right

        return root

    def inOrder(self, root):
        res = []
        if not root: return res
        
        stack = []
        curr = root
        while True:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                if not stack:
                    return res
                else:
                    curr = stack.pop()
                    res.append(curr.val)
                    curr = curr.right
                    
        
    def createList(self, l):
        if len(l) < 1:
            return None
        start = ListNode(l[0])
        weaver = start
        if len(l) > 1:
            for i in xrange(1, len(l)):
                weaver.next = ListNode(l[i])
                weaver = weaver.next
        return start

    def printList(self, l):
        templ = l
        value = []
        while templ != None:
            value.append(templ.val)
            templ = templ.next
        print value
        
if __name__ == "__main__":
    test = Solution()
    head = test.createList([1,2,3,4,5])
    root = test.sortedListToBST(head)
    print test.inOrder(root) 
