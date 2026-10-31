class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        class Node():
            def __init__(self, time, count, letter):
                self.time = time
                self.count = count
                self.letter = letter
            def __lt__(self, other):
                # if self.time == other.time:
                #     return self.count > other.count
                # return self.time < other.time
                return self.count > other.count
        
        heap = []
        m = {}
        for i in tasks:
            if i in m:
                m[i] += 1
            else:
                m[i] = 1
        q = collections.deque()
        for i in m:
            q.append(Node(0,m[i], m))
        curr = 0
        while len(heap) or len(q):
            while len(q) and q[0].time <= curr:
                pop = deque.popleft(q)
                heapq.heappush(heap, pop)
            if len(heap):
                pop = heapq.heappop(heap)
                if pop.count > 1:
                    pop.count-=1
                    pop.time=curr+n+1
                    q.append(pop)
            curr+=1

        return curr

        