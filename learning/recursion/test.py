
def findMaxConsecutiveOnes(nums: list[int]) -> int:
    maxCount = 0
    count = 0
    for num in nums:
        if num == 1:
            count += 1
        else:
            maxCount = max(maxCount, count)
            count = 0
    return max(maxCount, count)

if __name__ == '__main__':
    print(findMaxConsecutiveOnes([1,1,0,1,1,1])) # 3
