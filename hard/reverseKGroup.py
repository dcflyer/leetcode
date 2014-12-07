# -*- coding: utf-8 -*-
"""
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.

Only constant memory is allowed.

For example,
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

@author: Dennis
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def reverseKGroup(self, head, k):
        if not head: return head
        dummy = ListNode(0)
        dummy.next = head
        prev, curr, count = dummy, head, 0
        
        while curr:
            count += 1
            next = curr.next
            if 0 == count%k:
                prev = self.reverseRegion(prev, next)
            curr = next
            
        return dummy.next
        
#   reverse a region between prev and end, return the reversed last node 
#   (the one before next)
#   this is exactly the same as the reverse list below
#   there is another version of reverse list in reorderList.py
    def reverseRegion(self, prev, end):
        if not prev or not prev.next: return prev
        
        last, curr = prev.next, prev.next.next
        while curr != end:
            last.next = curr.next
            curr.next = prev.next
            prev.next = curr
            curr = last.next

        return last
    
    def reverseList(self, head):
        if not head: return head
        
        dummy = ListNode(0)
        dummy.next = head
        prev, last, curr = dummy, head, head.next
        while curr:
            last.next = curr.next
            curr.next = prev.next
            prev.next = curr
            curr = last.next
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
    start = test.createList([1,2,3,4,5])
    test.printList(test.reverseKGroup(start, 3))
        