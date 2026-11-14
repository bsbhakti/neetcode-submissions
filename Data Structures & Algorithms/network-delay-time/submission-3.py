class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        res = 0
        m = {}
        dist = [float('inf')] *n 
        for s,d,w in times:
            # #print(s,d,w)
            if s in m:
                m[s].append((d,w))
            else:
                m[s] = [(d,w)]
        #print(m)
        q = []
        heapq.heappush(q,(0,k) )

        # s = set()
        # s.add(k)

        while q:
            # total = len(q)
            # for _ in range(total):
                pop = heapq.heappop(q)
                #print("popped", pop)
                # s.add(pop[1])
                curr = pop[0]
                if dist[pop[1] - 1] > curr:
                    dist[pop[1] - 1] = curr
                    #print("s ", s)
                    res = max(curr,res)
                    if pop[1] in m:
                        for i in m[pop[1]]:
                            #print("curr", i)
                            # if i[0] not in s:
                            if dist[i[0]-1] > i[1] + curr:
                                heapq.heappush(q,(i[1] + curr, i[0])) 
                                #print("pushed")
                            

        if float('inf') in dist:
            return -1
        return res

        