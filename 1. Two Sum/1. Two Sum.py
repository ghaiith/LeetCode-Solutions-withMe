"""
@Author : Ghaith Ahmed

Runtime: 67 ms
Memory: 17.6 MB

"""
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_indices = {}  # Create an empty dictionary to store numbers and their indices

        for i, num in enumerate(nums):
            complement = target - num  # Calculate the complement for the current number
            if complement in num_indices:  # Check if the complement is already in the dictionary
                return [num_indices[complement], i]  # If found, return the indices of the two numbers
            num_indices[num] = i  # If not found, store the current number and its index in the dictionary

        return []  # If no solution is found, return an empty list
