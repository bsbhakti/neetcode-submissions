class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        visited = set()
        rows,cols = len(grid), len(grid[0])
        islands = 0

        def bfs(r,c):
            q = collections.deque()
            directions = [[-1,0],[1,0],[0,1], [0,-1]]
            q.append((r,c))
            visited.add((r,c))

            while q:
                # print("here",r,c)
                nr,nc = q.popleft()
                for d,w in directions:
                    row,col = nr+d,nc+w
                    # print(visited)
                    if((row,col) not in visited and 
                     row in range(rows) and col in range(cols) and grid[row][col] == "1"): 
                        # print("append", row,col)
                        q.append((row,col))
                        visited.add((row,col))
            # return

                

        for r in range(rows):
            for c in range(cols):
                if((r,c) not in visited and 
                grid[r][c] == "1"):
                    # print("going",r,c)
                    bfs(r,c)
                    islands +=1
        return islands
