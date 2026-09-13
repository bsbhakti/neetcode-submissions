class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        dp = {}
        def recur(i,j):
            #print("looking at ", i,j, curr)
            if (i,j) in dp:
                return dp[(i,j)]
            elif i >= m:
                #print("exceeded i", n-j)
                dp[(i,j)] = (n-j)
                return (n-j)
            elif j >= n:
                dp[(i,j)] =  (m-i)
                #print("exceeded j", m-i)
                return (m-i)
            elif word1[i] == word2[j]:
                a =  recur(i+1,j+1)
                dp[(i,j)] = a
                return a
            else: #not eq
                a = 1+ recur(i+1,j+1) # r
                b = 1+recur(i+1,j) #d
                c = 1+recur(i,j+1) #i
                dp[(i,j)] = min(a,b,c)
                return min(a,b,c)
        return recur(0,0)

        