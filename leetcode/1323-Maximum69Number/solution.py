class Solution:
    def maximum69Number (self, num: int) -> int:
        """  
        Approach:
        Convert the number to a string and iterate through its digits.
        Replace the first occurrence of '6' with '9' and convert it back to an integer.

        Time: O(n)
        Space: O(n)
        """
        num_str = str(num)
        if len(set(num_str)) == 1 and num_str[0] == '9':
            return num
        
        new_num = 0
        i = 0
        n = len(num_str) - 1

        for char in num_str:
            if char == '6':
                new_num += 9 * 10 ** n
                i+=1
                break
            else:
                new_num += int(char) * 10 ** n
            i+=1
            n-=1
        
        if i < len(num_str):
            new_num += int(num_str[i:])

        return new_num
