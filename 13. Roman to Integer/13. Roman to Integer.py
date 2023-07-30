"""
@Author : Ghaith Ahmed

Runtime: 53 ms
Memory: 16.2 MB

"""

class Solution:
    def romanToInt(self, s: str) -> int:
        # Dictionary mapping Roman numerals to their corresponding integer values
        RomanDic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        
        # Initialize a variable to store the final integer value
        Num = 0
        
        # Loop through each character in the input string 's'
        for i in range(len(s)):
            # Check if the current character is not a valid Roman numeral
            if s[i] not in RomanDic.keys():
                return 0  # Return 0 if an invalid Roman numeral is found
            
            # Check if the current Roman numeral is smaller than the next one
            if i < len(s) - 1 and RomanDic[s[i]] < RomanDic[s[i+1]]:
                # If so, subtract the current value from the total
                Num -= RomanDic[s[i]]
            else:
                # Otherwise, add the current value to the total
                Num += RomanDic[s[i]]
        
        # Return the final integer value
        return Num
