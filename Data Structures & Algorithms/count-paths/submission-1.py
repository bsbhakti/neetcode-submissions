class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        lastRow = [1] * n

        for i in range(m-1):
            rowAbove = [1] * n 
            for j in range(n-2,-1,-1):
                rowAbove[j] = rowAbove[j+1] + lastRow[j]
            lastRow = rowAbove
        return lastRow[0]