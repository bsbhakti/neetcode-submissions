# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        q = deque()
        ret = []
        if not root:
            return []
        q.append(root)
        while len(q):

            new = []

            l = len(q)
            
            while l > 0:

                pop = q.popleft()
                #print("popped ", pop.val)
                new.append(pop.val)
                
                if pop.left:
                    q.append(pop.left)
                if pop.right:
                    q.append(pop.right)
                l -=1
            #print("new lvel", ret)
            ret.append(new)
        return ret
        