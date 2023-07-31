"""
@Author : Ghaith Ahmed

Runtime: 44ms
Memory: 16.2 MB

"""
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
