##Given a string s, find the length of the longest substring without repeating characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charIndexes = {}
        maxLength = 0
        startIndex = 0
        
        for i, char in enumerate(s):
            if char in charIndexes and  startIndex <= charIndexes[char]:
                startIndex = charIndexes[char] + 1
            else:
                maxLength = max(maxLength, i - startIndex + 1)
            charIndexes[char] = i
        return maxLength
            
        
