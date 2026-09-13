class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        m = {}
        for src,dst in tickets:
            if src in m:
                heapq.heappush(m[src],dst)
            else:
                m[src] = [dst]
        
        # print(m)

        def recur(curr, res):
            if curr not in m:
                res.append(curr)
                return
            elif len(m[curr]) == 0:
                res.append(curr)
                return
            while len(m[curr]):
                top = heapq.heappop(m[curr])
                recur(top,res)
            res.append(curr)
        res = []
        recur("JFK",res)
        return res[-1::-1]
        