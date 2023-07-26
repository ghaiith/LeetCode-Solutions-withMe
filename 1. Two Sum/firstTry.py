"""
@Author : Ghaith Ahmed

Runtime: 608 ms
Memory: 17.3 MB

"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            if target-nums[i] in nums[i+1:]:
                firstNumber=i
                secondNumber=target-nums[i]
                nums.pop(firstNumber)
                return [firstNumber,nums.index(secondNumber)+1]
        return []

"""
Runtime: 608 ms
Memory: 17.3 MB

"""