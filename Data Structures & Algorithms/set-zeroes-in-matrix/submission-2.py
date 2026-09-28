from collections import deque
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m,n=len(matrix),len(matrix[0])
        def set_row(row:int):
            for j in range(n):
                matrix[row][j]=0
        def set_col(col:int):
            for i in range(m):
                matrix[i][col]=0
        
        # q=deque()
        row_array=[None]*m
        col_array=[None]*n

        # locate the 0(s)
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    row_array[i]=0
                    col_array[j]=0
        for r in range(len(row_array)):
            if row_array[r]==0:
                set_row(r)
        for c in range(len(col_array)):
            if col_array[c]==0:
                set_col(c)
        
        

        
        