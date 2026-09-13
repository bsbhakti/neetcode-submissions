class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m = len(grid)
        n = len(grid[0])
        def bfs(q):
            res = -1
            seen = set()
            #print("doing for ", i,j)

            while q: 
                length = len(q)
                res +=1
                for _ in range(length):
                    i,j = q.popleft()
                    seen.add((i,j))

                    #print("popped ", i,j)

                    if grid[i][j] != 0:
                        grid[i][j] = min(grid[i][j], res)
                        #print("set ", grid[i][j])

                    for k in [[1,0], [0,1], [-1,0], [0,-1]]:
                        new_i = i + k[0]
                        new_j = j + k[1]

                        if new_i < m and new_j < n and new_i >=0 and new_j >= 0 and (new_i, new_j) not in seen and grid[new_i][new_j] != 0 and grid[new_i][new_j] != -1 :
                            seen.add((new_i,new_j))
                            q.append((new_i,new_j))
        q = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                   q.append((i,j))
        bfs(q)
        return
