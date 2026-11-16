class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand = sorted(hand)
        #print(hand)
        arr = []
        m = {}
        for i in hand:
            if i in m:
                m[i] +=1
            else:
                arr.append(i)
                m[i] = 1
        i = 0
        #print(arr,m)
        while i < len(arr):
            reset = True
            curr = i
            #print("starting ",arr[i])
            for j in range(groupSize):
                
                if j != groupSize -1:
                    #print("checking in range for", arr[j+curr])
                    if curr+j+1 >= len(arr):
                        #print("greater", curr+j+1)
                        return False
                    
                    if arr[curr+j+1] -1 != arr[curr+j]:
                        #print("not con", arr[curr+j+1])
                        return False
                m[arr[curr+j]] -=1
                # #print(m)
                if m[arr[curr+j]] > 0 and reset:
                    reset = False
                    i +=j
                    #print("found new starting ", arr[i])
            if reset:
                i+=groupSize
                #print("new starting ", i)

        return True



        
        