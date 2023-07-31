# 20. Valid Parentheses

## Description

This is a Python solution to the problem of determining whether a given string of parentheses is valid or not. The `Solution` class provides a method named `isValid` for this purpose.

Given a string containing only the characters `'('`, `')'`, `'{'`, `'}'`, `'['`, and `']'`, the method `isValid` follows these steps to check the validity of the parentheses:
1. Initialize a dictionary `brackets_map` to map the closing brackets to their corresponding opening brackets.
2. Initialize an empty list `stack` to serve as a stack data structure.
3. Iterate through each character in the input string:
   - If the character is an opening bracket (`'('`, `'{'`, `'['`), push it onto the stack.
   - If the character is a closing bracket (`')'`, `'}'`, `']'`), pop the top element from the stack if it matches the corresponding opening bracket for this closing bracket.
   - If the stack is empty or the top element does not match the corresponding opening bracket, the parentheses are not valid, and the method returns `False`.
4. After iterating through all characters, if the stack is empty, it means all opening brackets have been matched with their corresponding closing brackets, and the method returns `True`. Otherwise, there are unmatched opening brackets, and the method returns `False`.

## Usage

To use the `isValid` method, follow these steps:

1. Import the `Solution` class from the provided code file.

   ```python
   class Solution(object):
       def isValid(self, s):
           # Implementation of the isValid method
   ```

2. Create an instance of the `Solution` class.

   ```python
   solution = Solution()
   ```

3. Call the `isValid` method with the string containing parentheses you want to check.

   ```python
   input_string = "{[()()]}"
   result = solution.isValid(input_string)
   ```

4. The `result` variable will contain `True` if the parentheses are valid and `False` otherwise.

## Example

```python
class Solution(object):
    def isValid(self, s):
        brackets_map = {')': '(', '}': '{', ']': '['}
        stack = []

        for char in s:
            if char in brackets_map.values():  # If it's an opening bracket
                stack.append(char)
            elif char in brackets_map:  # If it's a closing bracket
                if not stack or stack.pop() != brackets_map[char]:
                    return False

        return not stack  # If the stack is empty, all opening brackets have been matched

# Example usage:
solution = Solution()
input_string = "{[()()]}"
result = solution.isValid(input_string)
print(result)  # Output: True
```

## Complexity Analysis

The time complexity of the `isValid` method is O(n), where n is the length of the input string. The method iterates through each character in the string once. During each iteration, the method performs constant time operations, such as dictionary lookups and stack manipulations, which do not depend on the size of the input. Therefore, the overall time complexity is linear, O(n).

The space complexity is O(n), where n is the length of the input string. In the worst case, when the input string consists of only opening brackets (e.g., `"((("`, the stack will contain all the opening brackets, and its size will be proportional to the length of the input string. Similarly, if the input string contains alternating opening and closing brackets (e.g., `"[({})]"`), the stack will have a size of n/2, where n is the length of the input. In the best case, when the input string has balanced parentheses (e.g., `"()[]{}"`), the stack will be empty, and its size will be constant regardless of the input length.

Therefore, the space complexity of the method is O(n) due to the space required to store the stack. The additional space used by the `brackets_map` dictionary is constant and does not depend on the input size.

Overall, the solution has a time complexity of O(n) and a space complexity of O(n). It efficiently determines the validity of parentheses in the input string using a stack-based approach.