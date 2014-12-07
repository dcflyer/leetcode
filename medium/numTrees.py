# -*- coding: utf-8 -*-
"""
Given n, how many structurally unique BST's (binary search trees) that store values 1...n?

For example,
Given n = 3, there are a total of 5 unique BST's. 

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

@author: n609874
"""
#Cn is the number of Dyck words[2] of length 2n. A Dyck word is a string consisting of n X's and n Y's such that no initial segment of the string has more Y's than X's 
#Re-interpreting the symbol X as an open parenthesis and Y as a close parenthesis, Cn counts the number of expressions containing n pairs of parentheses which are correctly matched
#Cn is the number of different ways n + 1 factors can be completely parenthesized (or the number of ways of associating n applications of a binary operator). 
#Successive applications of a binary operator can be represented in terms of a full binary tree.[3] (A rooted binary tree is full if every vertex has either two children or no children.) It follows that Cn is the number of full binary trees with n + 1 leaves
#Cn is the number of non-isomorphic ordered trees with n vertices. (An ordered tree is a rooted tree in which the children of each vertex are given a fixed left-to-right order.)
#Cn is the number of monotonic paths along the edges of a grid with n × n square cells, which do not pass above the diagonal.

#Cn表示长度2n的dyck word的个数。Dyck word是一个有n个X和n个Y组成的字串，且所有的前缀字串皆满足X的个数大于等于Y的个数。以下为长度为6的dyck words:
# XXXYYY XYXXYY XYXYXY XXYYXY XXYXYY
#将上例的X换成左括号，Y换成右括号，Cn表示所有包含n组括号的合法运算式的个数：
#((())) ()(()) ()()() (())() (()())
#Cn表示有n个节点组成不同构二叉树的方案数。
#Cn表示所有在n × n格点中不越过对角线的单调路径的个数。

# C_n = (2n, n) - (2n, n + 1)
# C_0 = 1, C_{n+1} = \sum_{i = 0}^n C_i*C_{n - i}


# we can solve it in O(n^2) polynomial time, O(n) by using Catalan's formula
class Solution:
    # @return an integer
    def numTrees(self, n):
        if 0 == n: return 0
        
        res = [0]*(n + 1)
        res[0], res[1] = 1, 1
        
        for i in xrange(2, n + 1):
            for j in xrange(0, i):
                res[i] += res[j]*res[i - 1 - j]
        return res[n]
    
if __name__ == "__main__":
    test = Solution()
    print test.numTrees(4)
        
        
        