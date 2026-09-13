class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        new = ""
        maxLength = 0
        i = 0
        for i in range(i,len(s)):
            for j in range(i,len(s)):
                if(s[j] in new):
                    #move start
                    c = s[j]
                    indx = s.index(c,i)
                    i = indx+1
                    # print( indx)
                else:
                    new = s[i:j+1]
                    maxLength = max(maxLength, len(new))
        return(maxLength)

        