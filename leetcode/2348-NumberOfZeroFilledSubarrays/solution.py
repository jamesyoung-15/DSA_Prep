class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        """ 
        Approach:
        For each zero in the array, we can form new subarrays by extending the previous subarrays that ended with a zero.
        We maintain a count of current consecutive zeros and add that to the total count of subarrays.
        If we encounter a non-zero, we reset the current count.
        Eg: [0,0,0] -> subarrays: [0], [0,0], [0,0,0], [0], [0], [0] = 6
        [0,0,1,0] -> subarrays: [0], [0,0], [0], [0] = 4
         
        time: O(n)
        space: O(1)  
        """
        current_subarrays, total_subarrays = 0, 0

        for num in nums:
            if num == 0:
                current_subarrays += 1
                total_subarrays += current_subarrays
            else:
                current_subarrays = 0
        
        return total_subarrays