# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_value={}

        for letter in s:
            if letter not in dict_value:
                dict_value[letter]=1
            else:
                dict_value[letter]+=1
        for letter in t:
            if letter not in dict_value:
                return False
            else:
                dict_value[letter]-=1
        for value in dict_value.values():
            if value!=0:
                return False
        return True

# TC : O(N)