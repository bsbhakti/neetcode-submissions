class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            l = len(i)
            if 0<=l<=9:
                res+="1"
            elif 10<=l<=99:
                res+="2"
            else:
                res+="3"
            res += str(len(i))
            res += i
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        if not s:
            return []            
        i = 0
        ret = []
        print(s)
        i = 0

        while i < len(s):
            print("loop",s[i])
            length = int(s[i])
            n = i+length
            print("length is upto", n)
            count = ""
            i+=1
            while i <= n:
                count += s[i]
                i+=1
            count = int(count)
            print("count is", count, i)

            n = i+count
            curr = ""
            # i+=1
            while i < n:
                curr += s[i]
                i+=1                                        
            ret.append(curr)
            print(curr)
        return ret
            



