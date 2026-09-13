class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        m = {}
        partition = []
        curr = 0
        for ind,i in enumerate(s):
            if i not in m:
                m[i] = curr
                partition.append([1,ind])
                curr +=1
            else:
                current_par = m[i]
                # print(partition,current_par)
                end = partition[current_par][1]
                for j in range(end+1, ind+1):
                    old_par = m[s[j]]
                    # partition.pop(old_par)
                    if old_par != current_par:
                        partition[old_par] = [-1,-1]
                        m[s[j]] = current_par
                    partition[current_par][0] +=1
                partition[current_par][1] = ind
        res = []
        for i in partition:
            if i[0] != -1:
                res.append(i[0])
        return res