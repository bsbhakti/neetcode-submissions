class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero = False
        rows = len(matrix)
        cols = len(matrix[0])

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    if r == 0:
                        zero = True
                    else:
                        matrix[r][0] = 0
                    matrix[0][c] = 0
        
        for i in range(1,rows):
            for j in range(1,cols):
                if matrix[i][0] == 0:
                    matrix[i][j] = 0
                if matrix[0][j] == 0:
                    matrix[i][j] = 0

        if matrix[0][0] == 0:
            for i in range(rows):
                matrix[i][0] = 0

        

        if zero:
            for j in range(cols):
                matrix[0][j] = 0
        return 
        