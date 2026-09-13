class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
    
        check = [0,0,0]
        
        for i in triplets:
            prev_check = check[:]
            ok = True
            for j in range(len(i)):
                if i[j] == target[j]:
                    check[j] = 1
                if i[j] > target[j]:
                    ok = False
                    break
            if not ok:
                # print("changing", prev_check)
                check = prev_check
            
            if check == [1,1,1]:
                return True
        # if check == [1,1,1]:
        #         return True
        return False
        
