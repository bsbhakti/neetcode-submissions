class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        rows, cols = len(heights), len(heights[0])
        def dfs(r,c, prev, visit):
            if r <0 or c < 0 or r >= rows or c >= cols or (r,c) in visit or prev > heights[r][c] :
                return 
            visit.add((r,c))
            for i in [[1,0], [0,1], [0,-1], [-1,0]]:
                dfs(r+i[0], c+i[1], heights[r][c], visit )
        
        a,p = set(), set()

        for i in range(rows):
            dfs(i,0,heights[i][0],p)
            dfs(i,cols-1,heights[i][cols-1],a)


        res = []

        for j in range(cols):
            dfs(0, j, heights[0][j], p)
            dfs(rows-1, j, heights[rows-1][j], a)
        for i in range(rows):
            for j in range(cols):
                if (i,j) in p and (i,j) in a:
                    res.append([i,j])
        return res


            