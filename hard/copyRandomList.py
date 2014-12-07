# -*- coding: utf-8 -*-
"""
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.

@author: Dennis
"""
# Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode

#我们需要一个哈希表的原因是当我们访问一个结点时可能它的随机指针指向的结点还没有访问过，
#结点还没有创建，所以我们需要线性的额外空间。
## 1. recursive way with hash table
#    def copyRandomList(self, head):
#        if not head: return None
#        return self.helper(head, {})
#    
#    def helper(self, head, hashmap):
#        if not head: return None
#        if head in hashmap:
#            return hashmap[head]
#        
#        copy = RandomListNode(head.label)
#        hashmap[head] = copy
#        copy.next = self.helper(head.next, hashmap)
#        copy.random = self.helper(head.random, hashmap)
##        WRONG !!!
##        hashmap[head] = copy
#        
#        return copy

## 2. iterative way with hash table
#    def copyRandomList(self, head):
#        if not head: return None
#    
#        copy = RandomListNode(head.label)
##        insert None in hashmap, ow, hashmap[curr.random] may have error
#        hashmap = {None: None}
#        hashmap[head] = copy
##        hashmap = {head: copy}
#        curr, currnew = head.next, copy
#        while curr:
#            currnew.next = RandomListNode(curr.label)
#            hashmap[curr] = currnew.next
#            currnew = currnew.next
#            curr = curr.next
##            WRONG !!! update map first
##            hashmap[curr] = currnew.next
#        
#        curr, currnew = head, copy
#        while curr:
#            currnew.random = hashmap[curr.random]
#            curr = curr.next
#            currnew = currnew.next
#        
#        return copy
       
# 3. iterative way without hash table
    def copyRandomList(self, head):
        if not head: return None
        
        curr = head
        while curr:
            newNode = RandomListNode(curr.label)
            newNode.next = curr.next
            curr.next = newNode
            curr = newNode.next
        
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
## NOT A GOOD WAY TO SPLIT LIST !!!       
#        newHead = head.next
#        curr, currnew = head, newHead
#        while curr:
#            curr.next = currnew.next
#            curr = curr.next
#            if curr:
#                currnew.next = curr.next
#                currnew = currnew.next     
         
        newHead = head.next # just record and return
        curr = head        
        while curr:
            temp = curr.next
            curr.next = temp.next
            if temp.next:
                temp.next = temp.next.next
            curr = curr.next   
        return newHead

    def createList(self, l):
        if len(l) < 1:
            return None
        start = RandomListNode(l[0])
        weaver = start
        if len(l) > 1:
            for i in xrange(1, len(l)):
                weaver.next = RandomListNode(l[i])
                weaver = weaver.next
        return start
        
if __name__ == "__main__":
    test = Solution()
#    l = test.createList([1,3,5])
#    l.random = l.next.next
#    l.next.random = l
#    l.next.next.random = l.next
#    test.copyRandomList(l)
    test.copyRandomList(RandomListNode(-1))
