# -*- coding: utf-8 -*-
"""
Given a list, rotate the list to the right by k places, where k is non-negative.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.

@author: n609874
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
    def rotateRight(self, head, k):
        if not head: return head
        
        count, runner = 0, head
        while runner:
            runner = runner.next
            count += 1
        
        if k > count: k %= count
        
        walker, runner = head, head
        for i in xrange(k):
            runner = runner.next
#        WRONG !!! don't forget the non rotate case
        if not runner: return head
        
#       to make walker points to k - 1 node        
        while runner.next:
            walker = walker.next
            runner = runner.next

        runner.next = head
        head = walker.next
        walker.next = None 
        
        return head

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
    head = test.rotateRight(start, 4)
    test.printList(head)
        
        
        