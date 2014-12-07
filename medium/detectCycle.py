# -*- coding: utf-8 -*-
"""
Created on Tue Nov  4 03:52:07 2014
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Follow up:
Can you solve it without using extra space? 
@author: weichen
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

#fast step: f = X + nY + K
#slow step: s = X + mY + K
#           f = 2s
#           (n - 2m)Y = X + K

class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        if not head or not head.next:
            return None
        
        fast = head; slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                fast = head
                while fast!= slow:
                    fast = fast.next
                    slow = slow.next
                return fast
        return None
                    
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

if __name__ == "__main__":
    test = Solution()
    l = [1,3,5,8,10]
    head = test.createList(l)
    mid = head.next.next
    end = head.next.next.next.next
    end.next = mid    
        
    start = test.detectCycle(head)
    print start.val
        
        
            
