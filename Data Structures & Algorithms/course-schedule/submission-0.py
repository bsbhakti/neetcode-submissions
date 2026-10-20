class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        m = {}
        for i in prerequisites:
            course,pre = i[0],i[1]
            if course in m:
                m[course].append(pre)
            else:
                m[course] = [pre]
        #print(m)

        def dfs(curr, path, visited):
            #print("path", path, curr)
            if curr in visited:
                return True
            if curr in path:
                return False
            path.add(curr)
            if curr in m:
                for pre in m[curr]:
                    if pre in path:
                        return False
                    # path.add(pre)
                    a = dfs(pre,path,visited)
                    if not a:
                        #print(pre)
                        return False
                    if pre in path:
                        path.remove(pre)
            return True
        
        visited = set()
        for i in prerequisites:
            s = set()
            # s.add(i[0])
            #print("calling", i[0])
            a = dfs(i[0], s, visited)
            if not a:
                return False
            visited.update(s)
        return True
        