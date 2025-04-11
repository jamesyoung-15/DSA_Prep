
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


    def insert(self, root, val):
        if root is None:
            return TreeNode(val)

        if val > root.val:
            root.right = self.insert(root.right, val)
        else:
            root.left = self.insert(root.left, val)

        return root
    
    def removeNode(self, root, val):
        if root is None:
            return None
        
        

# test
def create_tree(arr):
    if not arr:
        return None
    root = TreeNode(arr[0])
    for i in arr[1:]:
        root.insert(root, i)
    return root

