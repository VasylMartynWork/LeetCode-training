# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def checkTree(self, root: TreeNode) -> bool:
        if(root.left + root.right == root.val):
            return True
        else:
            return False

nodes = TreeNode(10, 6, 4)
sol = Solution()
print(sol.checkTree(nodes))