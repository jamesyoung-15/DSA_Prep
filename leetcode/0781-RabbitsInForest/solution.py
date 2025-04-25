class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        # greedy approach: sort input and iterate through it, counting how many rabbits can be in same group
        # eg: [1,1,2] -> 1 group of size 2, group of size 3
        # time: O(nlogn), space: O(1)
        answers.sort() # sort to group rabbits that can have same colours
        result = 0
        count = 0 # count to see how many rabbits can be in same group

        for idx, answer in enumerate(answers):
            # if answer is 0 rabit is unique so add 1 to result
            if answer == 0:
                result+=1
            # start new colour group
            elif idx == 0 or answers[idx] != answers[idx-1] or count == 0:
                result += answer + 1 # add 1 cause including the rabbit that answered (How many OTHER rabbits have same color)
                count = answers[idx]
            # decrement if still part of group
            else:
                count -= 1
        return result 