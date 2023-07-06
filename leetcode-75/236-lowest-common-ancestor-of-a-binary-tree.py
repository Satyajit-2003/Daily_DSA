# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if root == p or root == q:
            return root

        a1 = self.lowestCommonAncestor(root.left, p, q)
        a2 = self.lowestCommonAncestor(root.right, p, q)

        if a1 and a2:
            return root
        if a1:
            return a1
        return a2