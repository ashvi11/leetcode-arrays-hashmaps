#1 Using alnum() and creating a new string
# We'll create a blank string and add only alpha-numeric characters. If the lowercase of new string and lowercase of reverse of new string are equal, return True

# TC = O(n)
# SC = O(n) (n for newStr, n for newStr{::-1], n+n = 2n ~ n)

class Solution:
    def isPalindrome(self, s: str) -> bool:
      newStr = ''
      
      for c in s:
        if s[c].isalnum():
          newStr += c
      
      return newStr.lower() != newStr[::-1].lower():

-----------------------------------------------------------------------------------------------------------------------------------------------------------------

#2 NEETCODE Best approach
# Use 2 pointers, left(l) and right(r). l = 0 and r = len(s) -1. Compare lowercase l and lowercase r. If these two are not equal, retun False, else increment l, 
# decrement right. If False is not returned at all, return True.
# To non-alphanumeric characters, follow this:
# Create a function to check if ASCII value of a chanracter c is between A-Z, a-z and 0-9. If it is, return True, else return False
# Call that function in the main code using sef.func(). If character is 'not' alphanumeric, go ahead one space(l)/ go back one space(r)

# TC = O(n) (linear)
# SC = O(1) (we are not using any extra space)

class Solution:
    def isPalindrome(self, s: str) -> bool:
      
      l = 0
      r = len(s) - 1
      
      while l < r:
        while l < r and not self.alphaNum(s[l]):
          l += 1
        while r > l and not self.alphaNum(s[r]):
          r -= 1
        if s[l].lower() != s[r].lower():
          return False
        l += 1
        r -= 1
        
      return True
    
    def alphaNum(self, c):
      return (ord('A') <= ord(c) <= ord('Z') or ord('a') <= ord(c) <= ord('z') or ord('0') <= ord(c) <= ord('9'))
    
    
----------------------------------------------------------------------------------------------------------------------------------------------------------------------
    
        
        
        
        
   
