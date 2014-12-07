# -*- coding: utf-8 -*-
"""
Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.


OJ's undirected graph serialization:
Nodes are labeled uniquely.

We use # as a separator for each node, and , as a separator for node label and each neighbor of the node.
As an example, consider the serialized graph {0,1,2#1,2#2,2}.

The graph has a total of three nodes, and therefore contains three parts as separated by #.

First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
Second node is labeled as 1. Connect node 1 to node 2.
Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a self-cycle.
Visually, the graph looks like the following:

       1
      / \
     /   \
    0 --- 2
         / \
         \_/
         
@author: Dennis
"""

# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node

## 1. BFS
#    def cloneGraph(self, node):
#        if not node: return None
#        
#        copy = UndirectedGraphNode(node.label)
#        hashmap = {node: copy}
#        queue = [node]
#        while queue:
#            curr = queue.pop(0)
#            for x in curr.neighbors:
#                if x not in hashmap:
#                    hashmap[x] = UndirectedGraphNode(x.label)
#                    queue.append(x)
##                WRONG!!!
##                hashmap[curr].neighbors.append(x)
#                hashmap[curr].neighbors.append(hashmap[x])
#        
#        return copy
            
## 2. DFS (exactly the same code with BFS)            
#    def cloneGraph(self, node):
#        if not node: return None
#                
#        copy = UndirectedGraphNode(node.label)
#        hashmap = {node: copy}
#        stack = [node]
#        
#        while stack:
#            curr = stack.pop()
#            for x in curr.neighbors:
#                if x not in hashmap:
#                    hashmap[x] = UndirectedGraphNode(x.label)
#                    stack.append(x)
#                hashmap[curr].neighbors.append(hashmap[x])
#        
#        return copy
        
# 3. DFS (recursion)   
    def cloneGraph(self, node):
        if not node: return None
                    
        return self.helper(node, {})

    def helper(self, node, hashmap):
        
        if node in hashmap:
            return hashmap[node]
        
        copy = UndirectedGraphNode(node.label)
        hashmap[node] = copy
        for x in node.neighbors:
            copy.neighbors.append(self.helper(x, hashmap))
        return copy
    