class Solution:
    def romanToInt(self, s: str) -> int:
        roman_int_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900
        }
        # iterate to len(s) - 1 as we want to look ahead for special cases
        result = 0
        i = 0
        while i<len(s):
            # check for special cases
            if s[i:i+2] in roman_int_dict and i<len(s)-1:
                result += roman_int_dict[s[i:i+2]]
                i+=2
            # otherwise just add the individual roman int
            else:
                result += roman_int_dict[s[i]]
                i+=1
        return result
    
# time: O(n), memory: O(n)

print(Solution().romanToInt('LVII'))