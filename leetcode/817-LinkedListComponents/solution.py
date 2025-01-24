# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        # convert nums to set, go through linked list and check if node in set
        # if node in set, increment num_seen, if not in set add to result only if num_seen greater than 0
        # outside loop if num_seen > 0 add to output for edge case (see example 1 [3])

        # time: O(n), space: O(n)
        nums_set = set()
        for num in nums:
            nums_set.add(num)
        
        curr = head
        num_seen = 0
        output = 0
        while curr:
            if curr.val in nums_set:
                num_seen += 1
            elif curr.val not in nums_set and num_seen > 0:
                output+=1
                num_seen = 0
            
            curr = curr.next
        if num_seen > 0:
            output+=1
        return output
            