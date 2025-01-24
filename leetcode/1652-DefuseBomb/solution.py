class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        # sliding window solution
        # for k != 0, compute k sliding window sum, update window as we move along and add it to result
        # time: O(n), space: O(n)
        n = len(code)
        result = [0] * n

        if k == 0:
            return result
        
        if k > 0:
            window_sum = sum(code[1:k+1])
            result[0] = window_sum
            for i in range(1,n):
                window_idx = i
                window_sum -= code[window_idx]
                if window_idx+1+k >= n:
                    window_idx = window_idx - n
                window_sum += code[window_idx+k]
                result[i] = window_sum
            return result
        
        if k < 0:
            window_sum = 0
            for i in range(n-1,n+k-1,-1):
                window_idx = i
                if window_idx < 0:
                    window_idx += n - 1
                window_sum += code[window_idx]
            result[0] = window_sum
            for i in range(n-1, -1, -1):
                window_idx = i
                window_sum -= code[window_idx]
                if window_idx+1+k < 0:
                    window_idx = window_idx + n
                window_sum += code[window_idx+k]
                result[i] = window_sum
            return result        
        
        
        # brute force solution time: O(n*k), space: O(n)
        # n = len(code)
        # result = [0] * n
        # if k == 0:
        #     return result
        
        # if k > 0:
        #     for i in range(n):
        #         for j in range(i+1,i+k+1):
        #             if j>=n:
        #                 j -=n
        #             result[i] += code[j]            
        # if k<0:
        #     for i in range(n):
        #         for j in range(i-1, i+k-1, -1):
        #             if j < 0:
        #                 j += n
        #             print(j)
        #             result[i] += code[j]

        # return result
        