# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = root.val
        def recur(node):
            nonlocal res
            if not node:
                return 0
            l = recur(node.left)
            r = recur(node.right)

            a = max(node.val, node.val+l, node.val+r)
            res = max(res,max(a, l+node.val+r))
            # print("ret", node.val,"->", a,res)
            return a
        recur(root)
        return res
        