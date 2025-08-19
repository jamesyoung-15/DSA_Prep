class Solution:
    def largestGoodInteger(self, num: str) -> str:
        """ 
        Go through 3 char at a time and see if it is good

        time: O(n) - as it goes through the string once w/ sliding window
        space: O(1) - max 3 char string is stored
        """
        curr_largest = ""
        curr_largest_int = 0
        for i in range(0, len(num) - 2):
            window = num[i:i+3]
            if window == "999":
                return "999"
            if len(set(window)) == 1:
                window_int = int(window)
                if window_int >= curr_largest_int:
                    curr_largest = window
                    curr_largest_int = window_int
        return curr_largest