class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        res = 0
        m = {}
        for s,d,w in times:
            # print(s,d,w)
            if s in m:
                m[s].append((d,w))
            else:
                m[s] = [(d,w)]
        print(m)
        q = []
        heapq.heappush(q,(0,k) )

        s = set()
        # s.add(k)

        while q and len(s) < n:
            # total = len(q)
            # for _ in range(total):
                pop = heapq.heappop(q)
                print("popped", pop)
                if pop[1] not in s:
                    s.add(pop[1])
                    curr = pop[0]
                    print("s ", s)
                    res = max(curr,res)
                    if pop[1] in m:
                        for i in m[pop[1]]:
                            print("curr", i)
                            if i[0] not in s:
                                heapq.heappush(q,(i[1] + curr, i[0])) 
                                print("pushed")
                            

        if len(s) != n:
            return -1
        return res

        