# -*- coding: utf-8 -*-
"""
Given a linked list, swap every two adjacent nodes and return its head. 

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3. 

Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed. 

@author: n609874
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        if not head or not head.next: return head
            
        dummy = ListNode(0); dummy.next = head
        prev, curr = dummy, head
        while curr and curr.next:
            temp = curr.next.next
            curr.next.next = curr
            prev.next = curr.next
            prev = curr
            curr.next = temp
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
    head = test.createList([1,2,3,4])
    test.printList(test.swapPairs(head))