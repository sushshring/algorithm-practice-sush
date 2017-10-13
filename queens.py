#!/usr/bin/env python
import numpy as np
a =[[0 for x in range(8)] for _ in range(8)]
board = np.array(a)
print(np.matrix(board))

board[0][0] = 1
n = 8
def placeQueensRec(r):
    if r > n:
        return True
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] != 1:
                if queenSum(board, i,j) < 1:
                    board[i][j] = 1
                    if placeQueensRec(r+1) == True:
                        return True
                    else:
                        board[i][j] = 0
    return False




def queenSum(b, row, col):
    return diagSum(b, row, col) + np.sum(b[:,col]) + np.sum(b[row])

def diagSum(arr, i, j):
    N = len(arr[0])
    diagonal = np.diag(arr, j-i)
    antidiagonal = np.diag(arr[:, ::-1], N-j-1-i)
    return np.sum(diagonal) + np.sum(antidiagonal)

placeQueensRec(1)
print(board)
