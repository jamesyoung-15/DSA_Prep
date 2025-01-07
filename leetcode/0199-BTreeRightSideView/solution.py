# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # using level order traversal from left to right, appending the rightmost node to result
        result = []
        deq = deque()

        if not root:
            return result
        
        deq.append(root)

        while len(deq)>0:
            num_level_nodes = len(deq) # number of nodes in the level
            for i in range(len(deq)):
                curr = deq.popleft()

                # if we reached the rightmost node
                if num_level_nodes-1 == i:
                    result.append(curr.val)

                if curr.left:
                    deq.append(curr.left)
                if curr.right:
                    deq.append(curr.right)


        return result