from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # using inorder traversal
        
        # iterative, O(n) time, O(h) space
        stack = []
        curr = root
        while curr or root:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            k-=1
            if k <= 0:
                return curr.val
            curr = curr.right

        
        # recursive way, O(h) time and space
        def recursive(root):
            stack = []
            def inorder(root):
                if not root:
                    return
                inorder(root.left)
                stack.append(root.val)
                inorder(root.right)
            inorder(root)
            return stack[k-1]
        # return recursive(root)

