'''
Given a string, find the length of the longest substring without repeating characters.

Example 1:
Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 

Example 2:
Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''
# My solution
class Solution:
    def length_of_longest_substring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        max_substr = s[0]
        n = 1
        maxlen = 1
        for c in range(1, len(s)):
            if s[c] not in max_substr:
                max_substr += s[c]
                n += 1
            else:
                maxlen = n if n > maxlen else maxlen
                max_substr = max_substr[max_substr.index(s[c])+1:] + s[c]
                n = len(max_substr)
        return maxlen if n < maxlen else n

# Given Solution
class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s) 
        ans = 0
        for i in range(n):
            for j in range(i+1, n):
                if self.allUnique(s, i, j):
                    ans = max(ans, j-i) 
        return ans
    
    def allUnique(self, s: str, start: int, end: int):
        unique = set()
        for i in range(start, end):
            c = s[i]
            return False if c in unique else unique.add(c) 
        return True