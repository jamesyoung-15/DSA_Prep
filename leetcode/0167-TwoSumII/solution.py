class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # two pointer solution
        # time: O(n)
        # space: O(1)
        left, right = 0, len(numbers)-1

        while left<right:
            total_sum = target - numbers[left] - numbers[right]
            if total_sum == 0:
                return [left+1, right+1]
            elif total_sum < 0:
                right -= 1
            else:
                left += 1