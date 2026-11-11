class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        m = {}
        if len(edges) != (n-1):
            return False
        for i in edges:
            if i[0] in m:
                m[i[0]].append(i[1])
            else:
                m[i[0]] = [i[1]]
            
            if i[1] in m:
                m[i[1]].append(i[0])
            else:
                m[i[1]] = [i[0]]
        vis = set()
        def dfs(curr, parent):
            print(curr)
            nonlocal vis
            if curr in vis:
                print("repeated", curr,vis)
                return False
            vis.add(curr)
            if curr in m:
                for i in m[curr]:
                    if i == parent:
                        continue
                    a = dfs(i,curr)
                    if not a:
                        print("repeated", curr,vis)
                        return False
            return True
        if not edges and n==1:
            return True
        dfs(edges[0][0],-1)
        if len(vis) != n:
            return False
        return True
                