class Solution:
    def baseNeg2(self, n: int) -> str:
        if n == 0: return "0"
        stack = []
        while n!=0:
            # print(n, n%2, (n-1)//2)
            stack.append(n%2) # computes current digit in base -2
            n = (n-1) // -2 # updates n for the next iteration, subtract 1 to adjust for negative base, divide by -2 to shift numbers
        # print(stack)

        # reverse stack and provide answer
        answer = ""
        for i in reversed(stack):
            answer+=str(i)
        return answer