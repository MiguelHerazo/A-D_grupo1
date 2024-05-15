#Given a NxN matrix of positive integers. There are only three possible moves from a cell Matrix[r][c].
def maximumPath(Matrix,n, i = 0, j=0):
    if i == n - 1 and j == n - 1:
        return Matrix[i][j]

    if i >= n or i < 0 or j >= n or j < 0:
        return 0

    return max(maximumPath(Matrix, n, i + 1, j),
               maximumPath(Matrix, n,i + 1, j - 1),
               maximumPath(Matrix,n, i + 1, j + 1)) + Matrix[i][j]

matrix = [[348,391], [618,193]]
n =2
maximumPath(matrix,n)
