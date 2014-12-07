# -*- coding: utf-8 -*-
"""
Given a sorted linked list, delete all duplicates such that each element appear only once. 

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3. 

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
        p = head
        while p != None:
            ### WRONG!!! if p.next != None and p.next.val == p.val:
            while p.next != None and p.next.val == p.val:
                p.next = p.next.next
            p = p.next
        
        return head
    
    def createList(self, l):
        head = ListNode(0)
        weaver = head
        for val in l:
            Node = ListNode(val)
            weaver.next = Node
            weaver = Node
        return head.next
    
    def printList(self, head):
        while head != None:
            print head.val
            head = head.next
            
if __name__ == "__main__":
    test = Solution()
    l = [2,3,1,3,4,5,1,2,1,0,2,1]
    l.sort()
    head = test.createList(l)
    test.printList(head)
    head = test.deleteDuplicates(head)
    test.printList(head)
    
            