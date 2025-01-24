# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # recursively check if both left and right subtrees are equal
        # time: O(min(n,m)), space: O(min(h1,h2)) b/c of call stack
        def dfs(p_node, q_node):
            if p_node is None and q_node is None:
                return True
            if (p_node is None and q_node is not None ) or (p_node is not None and q_node is None):
                return False
            if p_node.val == q_node.val:
                return dfs(p_node.left, q_node.left) and dfs(p_node.right, q_node.right)
            return False
        return dfs(p,q)
