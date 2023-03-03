#1 NEETCODE Best approach:
# Anagram means two strings have same characters, same number of times, but they are jumbled. This means the length should be the same. So first, we compare lengths of
# both the strings. IF they are not equal, they aren't Anagrams.
# Next we create two hashmaps(dictionaries), 1 for string s and 1 for string t. Create keys- each key will be each character in s, hence s[i]. If key is already 
# present, we 'get' that value and add 1. So, if the key is not already present, we would 'get' default value 0 and add 1. This way we create 2 hashmaps.
# Next, for each 'key'(c) in hashmap S, we comapre it's 'value'(countT[c]) in hashmap T. If that key is not present, return default value to 0.
# If values of those keys are not equal, return False. If False  isn't returned at all, return True.
# TC = O(n)
# SC = O(n)


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
        
       
----------------------------------------------------------------------------------------------------------------------------------------------------------------

#2 Same approach as above using Python functions, may not work in interviews. Above is the entire process coded as this
# TC = O(n)
# SC = O(n)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
    
---------------------------------------------------------------------------------------------------------------------------------------------------------------------

#3 For solve this problem in O(1) SC, we can sort the array, and compare it. TC depends on what sorting algorithm is used. It could be O(n^2)(for bubble sort) or best one- (nlogn).
#Good sorting algorithms has SC = O(n)(which has TC = nlogn), sometimes SC could be O(1). Normally Interviewers might consider sorting as O(1),
# so discuss this with him.
# TC = O(nlogn)- depending on sorting algorithm
# SC = O(1)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

#4 Follow up on 3.)- interviewer might ask to write your own sorting algorithm

-------------------------------------------------------------------------------------------------------------------------------------------------------------------






            
