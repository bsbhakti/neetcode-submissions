class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s)+1)
        dp[-1] = True

        for i in range(len(s)-1,-1,-1):
            for w in wordDict:
                print("checking up ",w, s[i:i+len(w)], len(s)-i >= len(w) )
                if len(s)-i >= len(w) and s[i:i+len(w)] == w:
                    dp[i] = dp[i+len(w)]
                    print("checking", s[i:], w, dp[i])

                if dp[i]:
                    break
        return dp[0]
