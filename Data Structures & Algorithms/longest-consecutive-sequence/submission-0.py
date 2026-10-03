class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0
        s = set()
        ret = 1
        for i in nums:
            s.add(i)
         
        for i in nums:
            if i in s:
                if i-1 not in s:
                    #starting point
                    #print("found start", i)
                    con = True
                    curr = 1
                    look = i+1
                    while con:
                        if look in s:
                            #print("found ne", i+1)
                            s.remove(look)
                            curr +=1
                            look = look+1

                        else:
                            con = False
                    ret = max(curr, ret)
        return ret
