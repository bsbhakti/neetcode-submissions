class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        res = []
        for i in triplets:
            ok = True
            for j in range(len(i)):
                if i[j] > target[j]:
                    ok = False
                    break
            if ok:
                res.append(i)
        check = [0,0,0]
        for i in res:
            for j in range(len(i)):
                if i[j] == target[j]:
                    check[j] = 1
                if check == [1,1,1]:
                    return True
        if check == [1,1,1]:
                return True
        return False
        
