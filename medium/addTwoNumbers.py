# -*- coding: utf-8 -*-
"""
You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8

@author: weichen
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        res = ListNode(0)
        p = res
        carry = 0
        while l1 or l2:
#            NOT GOOD ENOUGH, can combine carry with num
#            num = carry
#            if l1: 
#                num += l1.val
#                l1 = l1.next
#            if l2: 
#                num += l2.val    
#                l2 = l2.next
#            if num > 9:
#                carry = 1
#                num %= 10
#            else:
#                carry = 0
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
                
            p.next = ListNode(carry%10)
            carry /= 10
            p = p.next
            
        if carry == 1:
            p.next = ListNode(1)
        return res.next
    
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
    l1 = [2,4,3]; l2 = [5,6,4]
    List1 = test.createList(l1)
    List2 = test.createList(l2)
    test.printList(List1)
    test.printList(List2)
    List = test.addTwoNumbers(List1, List2)
    test.printList(List)
    
    
        