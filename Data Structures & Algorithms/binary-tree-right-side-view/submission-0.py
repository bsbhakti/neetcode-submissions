# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        curr = root
        ret = []
        q = deque()
        if not root:
            return []
        q.append(root)
        while len(q):
            length = len(q)
            while length >0:
                
                pop = q.popleft()
                if pop.left:
                        q.append(pop.left)
                if pop.right:
                        q.append(pop.right)
                if length == 1:
                    ret.append(pop.val)
                length -=1
        return ret


                   
    



        