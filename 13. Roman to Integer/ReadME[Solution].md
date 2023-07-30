# Roman to Integer Converter

## Description

This is a Python solution to the problem of converting Roman numerals to their corresponding integer values. The `Solution` class provides a method named `romanToInt` for this purpose.

Roman numerals use combinations of letters from the Latin alphabet to represent numbers. The basic Roman numerals and their integer equivalents are as follows:
- I: 1
- V: 5
- X: 10
- L: 50
- C: 100
- D: 500
- M: 1000

To convert a Roman numeral to an integer, the provided method `romanToInt` follows these steps:
1. Initialize a dictionary (`RomanDic`) to map each Roman numeral character to its corresponding integer value.
2. Initialize a variable (`Num`) to store the final integer value.
3. Loop through each character in the input Roman numeral string.
4. Check if the current character is not a valid Roman numeral. If an invalid character is found, the method returns 0.
5. Check if the current Roman numeral is smaller than the next one. If true, subtract the current value from the total (`Num`); otherwise, add the current value to the total.
6. Return the final integer value.

## Usage

To use the `romanToInt` method, follow these steps:

1. Import the `Solution` class from the provided code file.

   ```python
   class Solution:
       def romanToInt(self, s: str) -> int:
           # Implementation of the romanToInt method
   ```

2. Create an instance of the `Solution` class.

   ```python
   solution = Solution()
   ```

3. Call the `romanToInt` method with the Roman numeral string you want to convert.

   ```python
   roman_numeral = "XIV"
   result = solution.romanToInt(roman_numeral)
   ```

4. The `result` variable will contain the corresponding integer value of the input Roman numeral.

## Example

```python
class Solution:
    def romanToInt(self, s: str) -> int:
        RomanDic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        Num = 0
        for i in range(len(s)):
            if s[i] not in RomanDic.keys():
                return 0
            if i < len(s) - 1 and RomanDic[s[i]] < RomanDic[s[i+1]]:
                Num -= RomanDic[s[i]]
            else:
                Num += RomanDic[s[i]]
        return Num

# Example usage:
solution = Solution()
roman_numeral = "XIV"
result = solution.romanToInt(roman_numeral)
print(result)  # Output: 14
```

## Complexity Analysis

The time complexity of the `romanToInt` method is O(n), where n is the length of the input Roman numeral string. The method iterates through each character of the string once.

The space complexity is O(1) because the dictionary `RomanDic` and the variable `Num` occupy constant space regardless of the size of the input.