from typing import List

class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        output = 0
        # build tuple list of (label, value)
        test = []
        n = len(values)
        for i in range(n):
            test.append((labels[i],values[i]))

        # sort tuple list by values (descending)
        test.sort(key=lambda x:x[1], reverse=True)
        
        # build hashmap to keep track of number of times we use each label for useLimit
        hash_map = {}
        num_used = 0
        # go through tuple, add to hashmap, check if numWanted or useLimit exceeded, otherwise add to output
        for i in test:
            if num_used>=numWanted:
                break
            label = i[0]
            val = i[1]
            if label in hash_map and hash_map[label]>=useLimit:
                continue
            elif label in hash_map:
                hash_map[label] += 1
            else:
                hash_map[label] = 1
            output += val
            num_used += 1

        return output