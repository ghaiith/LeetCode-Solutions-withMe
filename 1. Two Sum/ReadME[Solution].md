# 1. Two Sum

## Description

This is a Python solution to the famous "Two Sum" problem. Given a list of integers and a target integer, the goal is to find two numbers in the list that add up to the target. The function `twoSum` takes a list of integers (`nums`) and an integer (`target`) as input and returns a list containing the indices of the two numbers that add up to the target. If no such pair is found, an empty list is returned.

## Usage

To use the `twoSum` function, follow these steps:

1. Import the `Solution` class from the provided code file.
   ```python
   from typing import List

   class Solution:
       def twoSum(self, nums: List[int], target: int) -> List[int]:
           # Implementation of the twoSum function
   ```

2. Create an instance of the `Solution` class.
   ```python
   solution = Solution()
   ```

3. Call the `twoSum` method with the list of integers (`nums`) and the target integer (`target`) as arguments.
   ```python
   nums = [2, 7, 11, 15]
   target = 9
   result = solution.twoSum(nums, target)
   ```

4. The `result` variable will contain a list of two indices, if a pair is found that adds up to the target. If no such pair is found, an empty list will be returned.

## Example

```python
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_indices = {}  # Store numbers and their indices in a dictionary

        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_indices:
                return [num_indices[complement], i]
            num_indices[num] = i

        return []

# Example usage:
solution = Solution()
nums = [2, 7, 11, 15]
target = 9
result = solution.twoSum(nums, target)
print(result)  # Output: [0, 1] (nums[0] + nums[1] = 2 + 7 = 9)
```

## Complexity Analysis

The time complexity of this solution is O(n) where n is the number of elements in the `nums` list. This is because we traverse the list once and perform constant-time operations for each element.

The space complexity is also O(n) as we use a dictionary (`num_indices`) to store the numbers and their indices in the worst-case scenario.

## Note

This solution assumes that there is exactly one valid solution, and each input would have exactly one solution. If there could be multiple valid solutions or the input list may have duplicate elements, additional checks or modifications might be required.