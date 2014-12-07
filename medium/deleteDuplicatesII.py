# -*- coding: utf-8 -*-
"""
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. 

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3. 

@author: n609874
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if not head or not head.next: return head
        
        dummy = ListNode(0)
        dummy.next = head
        prev, curr = dummy, head
        while curr:
            while curr.next and prev.next.val == curr.next.val:
                curr = curr.next
            if prev.next == curr:
                prev = curr
            else:
                prev.next = curr.next
            curr = curr.next
        
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
    head = test.createList([1,1,1,2,3,3,3])
    head = test.deleteDuplicates(head)
    test.printList(head)
    
                

        
        