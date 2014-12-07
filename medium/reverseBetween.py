# -*- coding: utf-8 -*-
"""
Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.

Note:
Given m, n satisfy the following condition:
1 ≤ m ≤ n ≤ length of list.

@author: Dennis
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
class Solution:
    # @param head, a ListNode
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    def reverseBetween(self, head, m, n):
#        in the reverse list, we don't need dummy node,
#        but we need one here
        dummy = ListNode(0)
        dummy.next = head
        
        prev = dummy
        count = 1
        while count < m: 
            prev = prev.next
            count += 1
        
#        prev points to m - 1 node
        newend = prev.next
        curr = newend
        newhead = None
        while curr and count <= n:
            temp = curr.next
            curr.next = newhead
            newhead = curr
            curr = temp
            count += 1
#        curr points to n + 1 node
        newend.next = curr
        prev.next = newhead
        return dummy.next
        
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
    head = test.createList([1,4,3,2,5,6])
    head = test.reverseBetween(head, 2, 4)
    test.printList(head)
        
        
        
        