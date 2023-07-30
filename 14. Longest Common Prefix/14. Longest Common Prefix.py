from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Check if there is only one string in the input list
        if len(strs) == 1:
            return strs[0]
        
        # Sort the list of strings by length to find the shortest string
        sorted_list = sorted(strs, key=len)
        
        # Dictionary to store the common prefixes and their occurrence count
        prefix_occurrences = {}
        
        # Iterate over the characters of the shortest string from the longest to the shortest
        for x in range(len(sorted_list[0]), 0, -1):
            # Compare the prefix of the shortest string with the prefix of other strings
            for i in range(len(sorted_list) - 1):
                if sorted_list[0][:x] == sorted_list[i + 1][:x]:
                    # If the prefix matches, update the occurrence count in the dictionary
                    if sorted_list[0][:x] in prefix_occurrences.keys():
                        prefix_occurrences[sorted_list[0][:x]] += 1
                    else:
                        prefix_occurrences[sorted_list[0][:x]] = 1
        
        # If no common prefix is found, return an empty string
        if not prefix_occurrences:
            return ''
        # If the maximum occurrence count is equal to the number of strings - 1,
        # return the common prefix with the maximum occurrence count
        elif max(prefix_occurrences.values()) == len(sorted_list) - 1:
            return max(prefix_occurrences, key=prefix_occurrences.get)
        else:
            # Otherwise, return an empty string indicating no common prefix
            return ""
