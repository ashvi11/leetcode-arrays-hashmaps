# NEETCODE Best solution:
# Create 2 pointers l and r at 0 index. Keep adding r to a new Set. As soon as we encouter a character during iteration that is already present in the set, 
# remove s[l] from set, and increment l.
# Keep adding s[r] to the set, calculating longest, and incrementing r in either case.

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
