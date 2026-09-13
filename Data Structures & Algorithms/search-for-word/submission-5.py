class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        path = set()
        rows = len(board)
        cols = len(board[0])
        def dfs(r,c,i):
            print(r,c,i)
            if(i == len(word)):
                return True
         
            if( r<0 or c<0 or r >=rows or c >= cols or i >=len(word) or board[r][c] != word[i] or 
            (r,c) in path ):
                 return False
            path.add((r,c))
            res = (dfs(r+1,c,i+1) or
            dfs(r-1,c,i+1)
             or dfs(r,c+1,i+1) 
             or dfs(r,c-1,i+1))
            path.remove((r,c))
            return res

        for i in range(len(board)):
            for j in range(len(board[0])):
                # print(i,j)
                if dfs(i,j,0):
                    return True
        return False




        