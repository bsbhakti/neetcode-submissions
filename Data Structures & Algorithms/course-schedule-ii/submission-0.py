class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        m = {}
        for i in prerequisites:
            curr = i[0]
            pre = i[1]
            if curr in m:
                m[curr].append(pre)
            else:
                m[curr] = [pre]
        #print(m)

        def dfs(curr, vis,ret, res_s):
            #print("checking curr", curr, "vis: ", vis, "ret: ", ret, "res_s:", res_s)
            if curr in vis:
                return False
            elif curr in res_s:
                return True
            vis.add(curr)
            if curr in m:
                for pre in m[curr]:
                    a = dfs(pre,vis,ret,res_s)
                    if not a:
                        return False
                    if pre in vis: vis.remove(pre)
                    
            ret.append(curr)
            res_s.add(curr)
            return True
        res_s = set()
        ret = []
        
        for i in range(numCourses):
            vis = set()

            a = dfs(i, vis,ret, res_s)
            if not a:
                return []
    
        return ret
            
            

        