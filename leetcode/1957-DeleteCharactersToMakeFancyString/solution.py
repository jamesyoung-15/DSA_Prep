class Solution:
    def makeFancyString(self, s: str) -> str:
        """ 
        Have 3 pointers, if they are all equal skip, otherwise add first pointer to result


        time: O(n)
        space: O(n) for result
        """

        if len(s) < 3:
            return s
        
        result = []
        ptr1 = 0
        ptr2 = 1
        ptr3 = 2
        while ptr3 < len(s):
            if not (s[ptr1] == s[ptr2] == s[ptr3]): result.append(s[ptr1])
            ptr1 += 1
            ptr2 +=1 
            ptr3 += 1
        result.append(s[ptr2-1])
        result.append(s[ptr3-1])

        return ''.join(result)