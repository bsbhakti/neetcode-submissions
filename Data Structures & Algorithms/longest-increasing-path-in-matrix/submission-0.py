class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = {}
        def recur(i,j,curr):
            ret = 1
            if (i,j) in dp:
                return dp[(i,j)]
            for k in [[1,0],[0,1],[-1,0],[0,-1]]:
                new_x = i+k[0]
                new_y = j + k[1]
                
                if new_x >= 0 and new_x < m and new_y >=0 and new_y < n and matrix[new_x][new_y] > matrix[i][j]:
                    # print("going from ", i,j, "to ",new_x,new_y )
                    ret = max(ret,1 + recur(new_x,new_y,curr+1))
            dp[(i,j)] = ret
            # print("ret",ret)
            return ret
        ret = 0
        for i in range(m):
            for j in range(n):
                # dp = {}
                ret = max(ret,recur(i,j,1))
        return ret

        