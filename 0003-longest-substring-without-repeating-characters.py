# NEETCODE Best solution:
# The concept is to find all substrings without repeating charaters that is present in the input. So we start with 1 character- point both l and r to index 0. 
# Now keep incrementing r and adding it to a new set if already not there. When r is on a character that is already in the set, increment l, and remove the previous l from the set
# Here l and r are formming a substring, that substring should not have any repeating characters, hence we keep incrementing l and removing previous l till all the characters between
# s[l] and s[r] are not unique.
# Keep calculating length by r-l+1
# Keep updating longest variable after each loop running once

# (The concept is to make a substring using l and r pointers, this substring shouldn't have repeating characters. So start by having both pointers at index 0, and keep incrementing r. 
# If a character is not already in the set, add it. If it's already in the set, that means we've encountered a repeating character. So the string needs to be shrinked. 
# So increment left pointer till we have all unique characters in the string. Now since our current string will have elements from current l to r, we need to remove previous l characters from the set. 
# Keep repeating until we reach the end of the string and update longest variable after each loop. length will be r-l+1)

# TC = O(n)
# SC = O(n) as we created a set

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
      charSet = set()
      l = 0
      longest = 0
      
      for r in range(len(s)):
        while s[r] in charSet:
          charSet.remove(s[l])
          l += 1
        charSet.add(s[r])
        longest = max(longest, r-l+1)
        r += 1
     return longest
        
-------------------------------------------------------------------------------------------------------------------------------------------------------------------
