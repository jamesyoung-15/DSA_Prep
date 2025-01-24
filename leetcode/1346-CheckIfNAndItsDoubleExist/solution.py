class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        # solution using hashmap, time: O(n), space: O(n)
        
        # create hashtable from original array,
        arr_map = {}
        for num in arr:
            if num not in arr_map:
                arr_map[num] = 1
            else:
                arr_map[num] += 1
        
        # loop through arr, check if 2 times current num exists
        for num in arr:
            double_num = 2*num
            # 0 edge case: if number is zero, we need to check if it occurred at least twice
            if double_num in arr_map and double_num == 0 and arr_map[double_num] >=2:
                return True
            if double_num in arr_map and double_num != 0:
                return True
        return False
        

        # brute force solution, time: O(n^2), space: O(1)
        # n = len(arr)
        # for i in range(n):
        #     for j in range(i+1,n):
        #         if arr[i] == 2*arr[j] or arr[j] == 2*arr[i]:
        #             return True
        # return False 