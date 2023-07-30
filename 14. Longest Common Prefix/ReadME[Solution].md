# 14. Longest Common Prefix

## Description

This is a Python solution to the problem of finding the longest common prefix among a list of strings. The `Solution` class provides a method named `longestCommonPrefix` for this purpose.

Given a list of strings, the method `longestCommonPrefix` follows these steps to find the longest common prefix:
1. If the list contains only one string, return that string as it is the common prefix.
2. Sort the list of strings in ascending order based on their lengths to find the shortest string.
3. Initialize an empty dictionary (`prefix_occurrences`) to store the common prefixes and their occurrence count.
4. Iterate through the characters of the shortest string from the longest to the shortest prefix.
5. Compare the prefix of the shortest string with the prefix of other strings in the list.
6. If a common prefix is found, update its occurrence count in the dictionary (`prefix_occurrences`).
7. After iterating through all prefixes, check if any common prefix was found:
   - If no common prefix is found, return an empty string.
   - If the maximum occurrence count in the dictionary is equal to the number of strings - 1, return the common prefix with the maximum occurrence count.
   - Otherwise, return an empty string indicating no common prefix was found.

## Usage

To use the `longestCommonPrefix` method, follow these steps:

1. Import the `Solution` class from the provided code file.

   ```python
   from typing import List

   class Solution:
       def longestCommonPrefix(self, strs: List[str]) -> str:
           # Implementation of the longestCommonPrefix method
   ```

2. Create an instance of the `Solution` class.

   ```python
   solution = Solution()
   ```

3. Call the `longestCommonPrefix` method with the list of strings you want to find the longest common prefix for.

   ```python
   input_strings = ["flower", "flow", "flight"]
   result = solution.longestCommonPrefix(input_strings)
   ```

4. The `result` variable will contain the longest common prefix among the input strings.

## Example

```python
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        
        sorted_list = sorted(strs, key=len)
        prefix_occurrences = {}
        
        for x in range(len(sorted_list[0]), 0, -1):
            for i in range(len(sorted_list) - 1):
                if sorted_list[0][:x] == sorted_list[i + 1][:x]:
                    if sorted_list[0][:x] in prefix_occurrences.keys():
                        prefix_occurrences[sorted_list[0][:x]] += 1
                    else:
                        prefix_occurrences[sorted_list[0][:x]] = 1
        
        if not prefix_occurrences:
            return ''
        elif max(prefix_occurrences.values()) == len(sorted_list) - 1:
            return max(prefix_occurrences, key=prefix_occurrences.get)
        else:
            return ''

# Example usage:
solution = Solution()
input_strings = ["flower", "flow", "flight"]
result = solution.longestCommonPrefix(input_strings)
print(result)  # Output: "fl"
```

## Complexity Analysis

The time complexity of the `longestCommonPrefix` method is O(n * m), where n is the number of strings in the input list, and m is the length of the shortest string. The method iterates through each character of the shortest string and compares it with the corresponding characters of other strings.

The space complexity is O(k), where k is the number of distinct common prefixes found in the input strings. The method uses a dictionary (`prefix_occurrences`) to store the common prefixes and their occurrence count. In the worst case, all strings have a unique prefix, resulting in k = n, where n is the number of strings in the input list. However, in the best case, where all strings have the same prefix, k would be 1.