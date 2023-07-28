"""
@Author : Ghaith Ahmed

Runtime: 82 ms
Memory: 16.4 MB

"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Check if the number is non-negative and its reverse is equal to itself
        # (the number is a palindrome).
        if x >= 0 and x == int(str(x)[::-1]):
            return True
        else:
            return False
