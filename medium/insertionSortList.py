# -*- coding: utf-8 -*-
"""
Sort a linked list using insertion sort.

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
#   WRONG!!! use helper header, o.w. a lot of cases
#    def insertionSortList(self, head):
#        
#        if not head or not head.next: return head
#        
#        piter = head.next
#        while piter:
#            p = head
#            if p.val < piter.val:
#                something!!!
#            while p.next != piter:
#                if p.next.val < piter.val:
#                    p = p.next
#                else:
#                    t = p.next
#                    p.next = piter
#                    piter = piter.next
#                    p.next.next = t
#                    continue
#            piter = piter.next
#        return head

    def insertionSortList(self, head):
        if not head: return head
    
        helper = ListNode(0)
        pre = helper
        curr = head
#        CODES to make it pass on leetcode
#        sorted = True
#        temp = head
#        while temp.next:
#            if temp.val > temp.next.val:
#                sorted = False
#                break
#            temp = temp.next
#        if sorted: return head
        
        while curr:
            next = curr.next
            pre = helper
            while pre.next and pre.next.val <= curr.val:
                pre = pre.next
            curr.next = pre.next
            pre.next = curr
            curr = next
        
        return helper.next
            
            
        
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
    test.printList(test.insertionSortList(head))  
        
