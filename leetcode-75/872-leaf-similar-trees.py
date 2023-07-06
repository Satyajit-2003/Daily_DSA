# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leaf_nodes(self, root: Optional[TreeNode]) -> List:
        leaves = []
        def dfs(root):
            if not root:
                return
            if not (root.left or root.right):
                leaves.append(root.val)
                return
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return leaves

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if self.leaf_nodes(root1) == self.leaf_nodes(root2):
            return True
        return False
