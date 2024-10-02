from typing import List
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # map count of student with 1s and 0s 
        cnts = {}
        for i in students:
            if i not in cnts:
                cnts[i] = 1
            else:
                cnts[i]+=1
        # go through sandwiches, decrement if in hashmap, if not in hashmap terminate early
        result = len(students)
        for s in sandwiches:
            if s in cnts:
                # student fed
                if cnts[s] != 0:
                    cnts[s] -= 1
                    result -= 1
                # no student wants sandwich
                else:
                    return result
            # no sandwich
            else:
                return result
        return result

# time: O(n), complexity: O(n)
students = [1,1,1,0,0,1]
sandwiches = [1,0,0,0,1,1]
test = Solution().countStudents(students,sandwiches)
print(test) # should be 3