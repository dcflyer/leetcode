# -*- coding: utf-8 -*-
"""
Given a 2D board containing 'X' and 'O', capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region. 

For example,


X X X X
X O O X
X X O X
X O X X

After running your function, the board should be: 

X X X X
X X X X
X X X X
X O X X

@author: n609874
"""

class Solution:
    # @param board, a 2D array
    # Capture all regions by modifying the input board in-place.
    # Do not return any value.

    
# time complexity O(mn), space complexity O(m + n)
    def solve(self, board):
        if not board: return
        
        self.nrow, self.ncol = len(board), len(board[0])
        for i in xrange(self.nrow):
            self.floodfill(board, i, 0)
            self.floodfill(board, i, self.ncol - 1)
        for j in xrange(self.ncol):
            self.floodfill(board, 0, j)
            self.floodfill(board, self.nrow - 1, j)
        
        for i in xrange(self.nrow):
            board[i] = map(lambda x: 'O' if '#' == x else 'X', board[i])
    
    def floodfill(self, board, row, col):
        if 'O' != board[row][col]:
            return
        board[row][col] = '#'
        import collections
#        WRONG !!! cannot create a deque with tuple
#        queue = collections.deque((row, col))
        queue = collections.deque()
        queue.append((row, col))
        while queue:
            index = queue.popleft()
            if index[0] > 0 and 'O' == board[index[0] - 1][index[1]]:
                queue.append((index[0] - 1, index[1]))
                board[index[0] - 1][index[1]] = '#'
            if index[0] < self.nrow - 1 and 'O' == board[index[0] + 1][index[1]]:
                queue.append((index[0] + 1, index[1]))
                board[index[0] + 1][index[1]] = '#'
            if index[1] > 0 and 'O' == board[index[0]][index[1] - 1]:
                queue.append((index[0], index[1] - 1))
                board[index[0]][index[1] - 1] = '#'
            if index[1] < self.ncol - 1 and 'O' == board[index[0]][index[1] + 1]:
                queue.append((index[0], index[1] + 1))
                board[index[0]][index[1] + 1] = '#'

if __name__ == "__main__":
    test = Solution()
    board = [['X' for i in xrange(4)] for j in xrange(4)]
    board[1][1] = board[1][2] = board[2][2] = board[3][1] = 'O'
    test.solve(board)
    print board
                
            


