# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        ret = None
        def recur(node):
            if not node:
                return 0
            elif not node.left and node.right:
                return 1
            l = recur(root.left)
            if l == k:
                ret = root.left.val
                return l+1
            elif l+1 == k:
                ret =  root.val
                return l+2
            elif l >k:
                return l+1
            else:
                r = recur(root.right)
                if r == k:
                    ret = root.right.val
                return l+r+1
        # recur(root)
        arr = []
        ret = None
        count = 0
        def inorder(node):
            nonlocal ret,count
            if not node:
                return 
            print(node.val)
            if not node.left and not node.right:
                arr.append(node.val)
                count +=1
                return 
            inorder(node.left)
  
            if count == k and ret is None:
                print("FOUND l", node.left.val)
                ret = node.left.val
                print(ret)
                return 
            count +=1
            if count == k:
                print("FOUND c", node.val)
                ret = node.val
                print(ret)
                return

            elif count > k:
                return 
            else:
                inorder(node.right) 
                if count == k and ret is None:
                    ret = node.right.val
                    print("FOUND r", node.right.val)
                    print(ret)

                return 
            
        if k == 1 and not root.left and not root.right:
            return root.val
        inorder(root)
        print(ret)

        return ret
        