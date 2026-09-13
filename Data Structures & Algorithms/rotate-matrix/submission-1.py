class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for ring in range(n//2):
            #ring
            #print("ring ",ring, "\n")
            for j in range(ring, n-1-ring):
                i = ring

                temp = matrix[i][j]
          
                #print("starting ", i, j)
                temp_i = i
                temp_j = j
                for _ in range(4):
                    #print(temp_i,temp_j,"->",temp_j,n-1-temp_i)
                    temp_r = matrix[temp_j][n-1-temp_i] 
                    matrix[temp_j][n-1-temp_i] = temp
                    temp = temp_r
                    old_j = temp_j
                    temp_j = n-1-temp_i
                    temp_i = old_j
                    #print("end", temp_i, temp_j)
        return 