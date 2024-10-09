class Solution:
    def isValid(self, s: str) -> bool:
        # first check if length is even, if it is odd then it is not valid
        if len(s)%2 != 0:
            return False
        # create a stack to hold open parentheses, then pop it whenever we get closing parentheses to check if it matches
        stack = []
        open_parentheses = ['(', '[', '{']
        for char in s:
            # if open parentheses, append to stack
            if char in open_parentheses:
                stack.append(char)
                continue
            # otherwise if it is closing parentheses, we check if stack exists, if it does check if it matches top of stack
            if not stack:
                return False
            else:
                top = stack.pop()
                if top == '(' and char!=')':
                    return False
                if top == '{' and char!='}':
                    return False
                if top == '[' and char!=']':
                    return False

        # check if stack has been fully popped (ie. if there was matching closing parentheses for opening parentheses)
        if stack:
            return False


        return True

# time: O(n), space: O(n)

s="[]"
print(Solution().isValid(s))