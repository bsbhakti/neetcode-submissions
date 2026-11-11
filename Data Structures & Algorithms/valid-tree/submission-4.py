class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        class DSU():
            def __init__(self,n):
                self.v = n
                self.parent = list(range(n+1))
                self.size = [1] * (n+1)
                self.comps = n
            
            def find(self,node):
                if self.parent[node] != node:
                    self.parent[node] = self.find(self.parent[node])
                return self.parent[node]
            
            def union(self,u,v):
                pu = self.find(u)
                pv = self.find(v)
                if pu == pv:
                    return False
                if self.size[pu] > self.size[pv]:
                    self.parent[pu] = pv
                    self.size[pu] += self.size[pv]
                else:
                    self.parent[pv] = pu
                    self.size[pv] += self.size[pu]
                self.comps -=1
                return True
            
            def com(self):
                return self.comps
        if len(edges) != n-1:
            return False
        dsu = DSU(n)
        for u,v in edges:
            if not dsu.union(u,v):
                return False
        return dsu.com() ==1            

                