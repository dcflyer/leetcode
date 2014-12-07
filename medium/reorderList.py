# -*- coding: utf-8 -*-
"""
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You must do this in-place without altering the nodes' values.

For example,
Given {1,2,3,4}, reorder it to {1,4,2,3}.

@author: Dennis
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
class Solution:
    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):
        if not head: return
        
        fast, slow = head, head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        
        
        head1, head2 = head, slow.next
        slow.next = None
        head2 = self.reverseList(head2)
#       NOT GOOD ENOUGH        
#        p1, p2 = head1, head2
#        while p1 and p2:
#            t1 = p1.next
#            t2 = p2.next
#            p1.next = p2
#            p2.next = t1
#            p1, p2 = t1, t2
        while head1 and head2:
            temp = head2.next
            head2.next = head1.next
            head1.next = head2
            head1 = head2.next
            head2 = temp
        
        return head   
        
# 1. iterative method        
    def reverseList(self, head):
        newhead = None
        curr = head
        
        while curr:
            temp = curr.next
            curr.next = newhead
            newhead = curr
            curr = temp
        return newhead
        
## 2. recursive method
## independent func works fine, but when works with reorderList,
## there is a runtime error, works fine locally        
#    def reverseList(self, head):
#        if not head: return head
#        
#        next = head.next
#        if not next: return head
#        
#        next = self.reverseList(next)
#        head.next.next = head
#        head.next = None
#        return next
        
       
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
    start = test.createList([1,2,3,4,5,6])
    start = test.reorderList(start)
#    start = test.reverseList(start)
    test.printList(start)

    
        
                
        
        
        
        
        
        
        