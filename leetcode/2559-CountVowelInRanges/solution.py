class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = {"a","e","i","o","u"}
        prefix_sum = [0]
        i = 1
        for word in words:
            if word[0] in vowels and word[-1] in vowels:
                prefix_sum.append(prefix_sum[i-1] + 1)
            else:
                prefix_sum.append(prefix_sum[i-1])
            i+=1 
        # print(prefix_sum)
        answer = []
        for query in queries:
            answer.append(prefix_sum[query[1] + 1] - prefix_sum[query[0]])
        return answer