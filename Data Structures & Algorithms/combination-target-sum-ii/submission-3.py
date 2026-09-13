class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        m = {}
        res = []

        itr = []
        

        for i in candidates:
            if i not in m:
                m[i] = 1
                itr.append(i)
            else:
                m[i] +=1
        # print("itr", itr,m)
        
        def recur(i, my_map, left,curr):
            # print(i, left, curr)
            if left == 0:
                res.append(curr[:])
                return
            elif i >= len(itr) or left < 0:
                return 
            else:
                for ind in range(i, len(itr)):
                    if my_map[itr[ind]] >0:
                        my_map[itr[ind]] -=1
                        curr.append(itr[ind])
                        recur(ind, my_map, left-itr[ind], curr )
                        my_map[itr[ind]] +=1
                        curr.pop()
        recur(0, m, target, [])
        return res




        