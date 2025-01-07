# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        # recursive
        def helper(root):
            if not root:
                return
            helper(root.left)
            result.append(root.val)
            helper(root.right)
        # helper(root)


        # iterative
        stack = []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            result.append(curr.val)
            curr = curr.right
        
        return result
    
# time: O(h), space: O(h), h is height of tree