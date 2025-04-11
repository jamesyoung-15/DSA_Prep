class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        # solution: go through each digit between low and high, split digit in half, check if even length, sum up to check if symmetric
        # time: O(n*m) where n is high-low and m is total digits, space: O(1)

        result = 0
        for i in range(low, high+1):
            num_str = str(i)
            if len(num_str) %2 != 0:
                continue
            first_half = num_str[:len(num_str)//2]
            second_half = num_str[len(num_str)//2:]
            first_half_sum = 0
            second_half_sum = 0
            for digit in first_half:
                first_half_sum += int(digit)
            for digit in second_half:
                second_half_sum += int(digit)
            if first_half_sum == second_half_sum:
                result+=1
            
            

        return result