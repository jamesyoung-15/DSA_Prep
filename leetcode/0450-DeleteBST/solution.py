from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        # base
        if not root:
            return root

        # search node to delete
        if key>root.val:
            root.right = self.deleteNode(root.right,key)
        elif key<root.val:
            root.left = self.deleteNode(root.left,key)
        # found node to delete
        else:
            # for 0 child or 1 right child, return right child
            if root.left is None:
                return root.right
            # for 1 left child, return left child
            elif root.right is None: 
                return root.left
            # two children, find min in right subtree
            else:
                # go to leftmost node in rightsubtree
                curr = root.right
                while curr.left:
                    curr = curr.left
                # swap val with delete node val
                root.val = curr.val
                # update rightsubtree recursively, where we delete the swapped value
                root.right = self.deleteNode(root.right,root.val)
        return root
# time: O(h) for BST height
# space: O(h) for recursion stack