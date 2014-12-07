# -*- coding: utf-8 -*-
"""
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.

@author: Dennis
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
class Solution:
    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode
    def partition(self, head, x):
        if not head: return head
                
        small, large = ListNode(0), ListNode(0)
        sIter, lIter = small, large
        while head:
            if head.val < x:
                sIter.next = head
                sIter = sIter.next
            else:
                lIter.next = head
                lIter = lIter.next
            head = head.next
            
        sIter.next = large.next
#        Don't forget this line
        lIter.next = None
        return small.next
        
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
    start = test.createList([1,4,3,2,5,2]) 
    test.printList(start)
    start = test.partition(start, 3)
    test.printList(start)
    