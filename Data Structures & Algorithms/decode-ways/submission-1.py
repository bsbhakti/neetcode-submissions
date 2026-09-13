class Solution:
    def numDecodings(self, s: str) -> int:
        total = {len(s): 1}

        def sol(i):
            if i in total:
                return total[i]
            if s[i] == "0":
                return 0
            
            res = sol(i+1)
            if(i+1 < len(s) and ((s[i] == "1") or (s[i] == "2") and s[i+1] in "0123456") ):
                res += sol(i+2)
            total[i] = res
            return res
        return sol(0)

        