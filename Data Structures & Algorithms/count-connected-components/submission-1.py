class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        m = {}
        res = 0
        for s,d in edges:
            if s in m:
                m[s].append(d)
            else:
                m[s] = [d]
            if d in m:
                m[d].append(s)
            else:
                m[d] = [s]
            
        vis = set()
        def dfs(curr, parent):
            vis.add(curr)
            if curr in m:
                for i in m[curr]:
                    if i not in vis and i != parent:
                        dfs(i, curr)
        
        for i in m:
            if i not in vis:
                dfs(i,-1)
                res +=1
        res += (n-len(vis))
        return res


        