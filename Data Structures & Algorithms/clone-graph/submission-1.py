"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
         q = collections.deque()
         if not node:
             return None
         q.append(node)
         visit = {}
        #  print(node.val,node.neighbors)

         while q:
            n = q.popleft()
            if(n not in visit):
                new = Node(n.val)
                visit[n] = new
            else:
                new = visit[n]


            # visit.add(n.val)
            for neighbour in n.neighbors:
                print("new")
                print("val",n.val)
                print("neigh",neighbour.val)
                if(neighbour not in visit):
                    print("in")
                    adj = Node(neighbour.val)
                    q.append(neighbour)
                    visit[neighbour] = adj
                    new.neighbors.append(adj)
                    print( adj.val)
                else:
                    new.neighbors.append(visit[neighbour])
                    print( visit[neighbour].val)

         return visit[node]
                
        