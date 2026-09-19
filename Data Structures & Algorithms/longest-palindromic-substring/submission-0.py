class Solution:
    def longestPalindrome(self, s: str) -> str:
        def palindrome(start,end):
            i = start-1
            j = end+1
            while i>=0 and j < len(s):
                if s[i] == s[j]:
                    i-=1
                    j+=1
                else:
                    # print("ret", i+1, j-1)
                    return s[i+1:j]
            # if i < 0:
            #     i +=1
            # if j >= len(s):
            #     j -=1
            # print("ex", i+1, j-1)
            return s[i+1:j]
        
        res = 0
        ret = None
        for i in range(len(s)):
            a = palindrome(i,i)
            if len(a) > res:
                res = len(a)
                ret = a
            if i != len(s)-1:
                if s[i] == s[i+1]:
                    a = palindrome(i,i+1)
                    if len(a) > res:
                        res = len(a)
                        ret = a
        return ret
            

