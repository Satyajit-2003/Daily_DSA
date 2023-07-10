# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.zigzag = 0
        def dfs(root, dir, zig):
            if not root:
                return
            self.zigzag = max(self.zigzag, zig)
            if dir == 'L':
                dfs(root.right, 'R', zig + 1)
                dfs(root.left, 'L', 1)
            else:
                dfs(root.left, 'L', zig + 1)
                dfs(root.right, 'R', 1)
        
        dfs(root.left, 'L', 1)
        dfs(root.right, 'R', 1)

        return self.zigzag
