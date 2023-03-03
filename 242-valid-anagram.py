#1 NEETCODE Best approach:
# Anagram means two strings have same characters, same number of times, but they are jumbled. This means the length should be the same. So first, we compare lengths of
# both the strings. IF they are not equal, they aren't Anagrams.
# Next we create two hashmaps(dictionaries)


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      if len(s) != len(t):
        return False
      
      countS, countT = {}, {}
      
      for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)
        
       for c in countS:
        if countS[c] != countT.get(c, 0):
          return False
        
       return True
        
       
