# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def include_root(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        ans = 0
        if root.val == targetSum:
            ans +=1
        ans += self.include_root(root.left, targetSum-root.val)
        ans += self.include_root(root.right, targetSum-root.val)
        return ans

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        return  (self.pathSum(root.left, targetSum) + 
                self.include_root(root, targetSum) + 
                self.pathSum(root.right, targetSum))