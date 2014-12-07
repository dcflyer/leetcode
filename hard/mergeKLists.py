# -*- coding: utf-8 -*-
"""
Created on Sat Nov 22 11:08:42 2014

@author: Dennis
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
class Solution:
    # @param a list of ListNode
    # @return a ListNode

## 1. transform the problem into merge 2 sorted list
##T(k) = 2T(k/2)+O(n*k)。根据主定理，可以算出算法的总复杂度是O(nklogk)。
##空间复杂度的话是递归栈的大小O(logk)。
#    def mergeKLists(self, lists):
#        if not lists: return None        
#        
#        return self.helper(lists, 0, len(lists) - 1)
#    
#    def helper(self, lists, l, r):
#        if l < r:
#            m = (l + r)//2
#            return self.merge(self.helper(lists, l, m), \
#                    self.helper(lists, m + 1, r))
#        return lists[l]
#    
#    def merge(self, l1, l2):
#        returnl = ListNode(0)
#        
#        it = returnl
#        while l1 and l2:
#            if l1.val < l2.val:
#                it.next = l1
#                l1 = l1.next
#            else:
#                it.next = l2
#                l2 = l2.next
#            it = it.next
#        
#        it.next = l1 if not l2 else l2
#        
#        return returnl.next
    
# 2. use heap        
    def mergeKLists(self, lists):
        import heapq
        if not lists: return None
    
        heap = []
        for head in lists:
            if head:
                heap.append((head.val, head))
        heapq.heapify(heap)
        
        returnl = ListNode(0); it = returnl
        while heap:
            pop = heapq.heappop(heap)
            it.next = pop[1]
            it = it.next
            if pop[1].next:
                heapq.heappush(heap, (pop[1].next.val, pop[1].next))
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
    l = test.mergeKLists([l1, l2])
    test.printList(l)    
    
        
        
        
    
        
        