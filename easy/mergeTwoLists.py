# -*- coding: utf-8 -*-
"""
Created on Thu Oct 30 10:25:50 2014

Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

@author: n609874
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        returnl = ListNode(0)
        t = returnl
        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                t.next = l1
                l1 = l1.next
            else:
                t.next = l2
                l2 = l2.next
            t = t.next
        
        t.next = l2 if l1 == None else l1
        return returnl.next

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
    A = [1,3,5,7,9]
    B = [2,4,6,8,10]
    l1 = test.createList(A)
    l2 = test.createList(B)
    test.printList(l1)
    test.printList(l2)
    l = test.mergeTwoLists(l1, l2)
    test.printList(l)    
    