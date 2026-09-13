class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cache = {}
        def recur(i,curr):
            if (i,curr) in cache:
                return cache[(i,curr)]
            elif i >= len(s):
                if curr == "":
                    cache[(i,curr)] = True
                    return True
                cache[(i,curr)] = False
                return False
            curr += s[i]
            if curr in wordDict:
                a = recur(i+1,curr)
                b = recur(i+1, "")
                cache[(i,curr)] = a or b
                return a or b
            else:
                a = recur(i+1, curr)
                cache[(i,curr)] = a
                return a
        return recur(0,"")
        