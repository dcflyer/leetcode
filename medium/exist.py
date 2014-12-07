# -*- coding: utf-8 -*-
"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

For example,
Given board =

[
  ["ABCE"],
  ["SFCS"],
  ["ADEE"]
]
word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.

@author: Dennis
"""

class Solution:
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
#    def exist(self, board, word):
#        if not word: return True
#        if not board or 0 == len(board) or 0 == len(board[0]): return False
#        
#        for i in xrange(len(board)):
#            for j in xrange(len(board[i])):
#                if board[i][j] == word[0]:
#                    if self.dfs(i, j, board, word[1:]):
#                        return True
#        
#        return False
#    
#    def dfs(self, i, j, board, word):
#        if not word: return True
#            
##        UP
#        if i > 0 and board[i - 1][j] == word[0]:
#            temp = board[i][j]
#            board[i][j] = '#'
#            if self.dfs(i - 1, j, board, word[1:]):
#                return True
#            board[i][j] = temp
#        
##        DOWN
#        if i < len(board) - 1 and board[i + 1][j] == word[0]:
#            temp = board[i][j]
#            board[i][j] = '#'
#            if self.dfs(i + 1, j, board, word[1:]):
#                return True
#            board[i][j] = temp
#            
##        LEFT
#        if j > 0 and board[i][j - 1] == word[0]:
#            temp = board[i][j]
#            board[i][j] = '#'
#            if self.dfs(i, j - 1, board, word[1:]):
#                return True
#            board[i][j] = temp
#
##        RIGHT
#        if j < len(board[0]) - 1 and board[i][j + 1] == word[0]:
#            temp = board[i][j]
#            board[i][j] = '#'
#            if self.dfs(i, j + 1, board, word[1:]):
#                return True
#            board[i][j] = temp            
#        return False

    def exist(self, board, word):
        if not word: return True
        if not board or 0 == len(board) or 0 == len(board[0]): return False
        
        visited = [[False for j in xrange(len(board[0]))] for i in xrange(len(board))]
        
        for i in xrange(len(board)):
            for j in xrange(len(board[i])):
                if self.dfs(i, j, word, board, visited):
                    return True
        
        return False
    
    def dfs(self, i, j, word, board, visited):
        if not word: return True
        
        if i < 0 or j < 0 or i > len(board) - 1 or j > len(board[0]) - 1 \
            or board[i][j] != word[0] or visited[i][j]:
                return False
        
        visited[i][j] = True
        res = self.dfs(i + 1, j, word[1:], board, visited) or \
            self.dfs(i - 1, j, word[1:], board, visited) or \
            self.dfs(i, j + 1, word[1:], board, visited) or \
            self.dfs(i, j - 1, word[1:], board, visited)
        visited[i][j] = False
        return res
        
        
if __name__ == "__main__":
    test = Solution()
    board = [ list("ABCE"), list("SFCS"), list("ADEE") ]
    print test.exist(board, "ABCCED")
    board = [ list("ABCE"), list("SFCS"), list("ADEE") ]
    print test.exist(board, "SEE")
    board = [ list("ABCE"), list("SFCS"), list("ADEE") ]
    print test.exist(board, "ABCB")