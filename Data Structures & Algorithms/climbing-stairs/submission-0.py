class Solution:
    def climbStairs(self, n: int) -> int:
        a = 2
        b = 3
        if n ==2:
            return 2
        if n==1:
            return 1

        for i in range(3,n):
            print(i)
            new_b = a + b
            a = b
            b = new_b
            print(b)
        return b


        