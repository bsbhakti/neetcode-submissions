# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        res = None
        def recur(node):
            nonlocal res
            if not node:
                return 0
            elif res is not None:
                return 0
            else:
                a = 0
                if node == p or node==q:
                    a = 1
                a += recur(node.left) + recur(node.right)
                if a == 2:
                    res = node
                    return 0
                return a
        recur(root)
        return res
          
            
        