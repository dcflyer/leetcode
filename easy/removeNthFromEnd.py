# -*- coding: utf-8 -*-
"""
Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:
Given n will always be valid.
Try to do this in one pass. 

@author: n609874
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        if not head: return head
        
        p1 = head; p2 = head
        for i in xrange(n):
            if not p2:
                return head
            p2 = p2.next
        
        if not p2: return head.next
            
        while p2.next:
            p1 = p1.next
            p2 = p2.next
        
#       now p1 points to the last n-1 th
        p2 = p1.next
        p1.next = p2.next
        p2.next = None
        return head
    
    def createList(self, l):
        head = ListNode(0)
        weaver = head
        for i in l:
            weaver.next = ListNode(i)
            weaver = weaver.next
        
        return head.next
    
    def printList(self, head):
        while head:
            print head.val,
            head = head.next
        print '\n'

if __name__ == "__main__":
    test = Solution()
    lList = [[1,2,3,4,5], [], [1,2], [1]]
    for l in lList:
        head = test.createList(l)
        head = test.removeNthFromEnd(head, 2)
        test.printList(head)
        
