class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        # two pointer approach: move right pointer until right before number that is not +1 increment, if left == right then just append number, otherwise append "left number -> right number"
        # time: O(n), space: O(n)
        n = len(nums)
        result = []
        left = 0
        while left<n:      
            right = left
            while right < n-1 and nums[right]+1 == nums[right+1]:
                right+=1
            if left == right:
                result.append(str(nums[left]))
            else:
                temp = str(nums[left]) + "->" + str(nums[right])
                result.append(temp)
            left = right
            left+=1
            
        return result