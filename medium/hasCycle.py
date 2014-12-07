# -*- coding: utf-8 -*-
"""
Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space? 

@author: weichen
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        if not head or not head.next:
            return False
        
        fast = head; slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False
        
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
        
    print test.hasCycle(head)      