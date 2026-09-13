class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def bfs(i,j):
            q = deque()
            q.append((i,j))
            res = 0
            seen = set()
            seen.add((i,j))
            grid[i][j] = 0

            while q:
                i,j = q.popleft()
                res +=1
                grid[i][j] = 0
                # print("pooped", i,j)
                for k in [[1,0],[0,1],[-1,0],[0,-1]]:
                    new_i = i+k[0]
                    new_j = j+k[1]
                    

                    if new_i <m and new_j <n and new_i >=0 and new_j >= 0 and grid[new_i][new_j] == 1 and (new_i,new_j) not in seen:
                        seen.add((new_i,new_j))
                        q.append((new_i, new_j))
            return res
        m = len(grid)
        n = len(grid[0])
        ret = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    ret = max(ret,bfs(i,j))

        return ret

        