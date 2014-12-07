# -*- coding: utf-8 -*-
"""
Sort a linked list in O(n log n) time using constant space complexity.

@author: weichen
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def sortList(self, head):
#       WRONG1!! Don't miss this line        
        if not head or not head.next: return head
            
        pfast = head; pslow = head
#       WRONG!!! check fast!!! next comes before next.next
#        while pfast.next.next and pslow.next:
        while pfast.next and pfast.next.next:
            pfast = pfast.next.next
            pslow = pslow.next
        
        pfast = pslow
        pslow = pslow.next
        pfast.next = None
        
        pfast = self.sortList(head)
        pslow = self.sortList(pslow)
        
        return self.mergeTwoLists(pfast, pslow)

    def mergeTwoLists(self, p1, p2):
        if not p1: return p2
        if not p2: return p1

        head = ListNode(0)
        p = head
        while p1 and p2:
            if p1.val < p2.val:
                p.next = p1
                p1 = p1.next
            else:
                p.next = p2
                p2 = p2.next
            p = p.next
        
        if p1: p.next = p1
        if p2: p.next = p2    
            
        return head.next  

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
    l = [1,3,5,8,10,2,4,6,7,9]
    head = test.createList(l)
    test.printList(test.sortList(head))                