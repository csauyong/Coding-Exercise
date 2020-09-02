#!/usr/bin/env python
"""LeetCode#3.py: find the length of the longest substr without repeating characters"""
def lengthOfLongestSubstring(s):
    maxLength = 0
    for i in range(len(s)):
        currLength = 0
        substring = ''
        duplicate = False
        for k in range(i,len(s)):
            for j in substring:
                if s[k] == j:
                    duplicate = True
            if not duplicate:
                substring += s[k]
                currLength += 1
            else:
                break
            if currLength > maxLength:
                maxLength = currLength
    return maxLength

print(lengthOfLongestSubstring(s = 'a'))
