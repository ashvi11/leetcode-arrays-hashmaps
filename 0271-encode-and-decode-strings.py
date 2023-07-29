# NEETCODE Best Solution:
# The question asks us to write a code to encode a list of string into a single string, and write a code to decode that string back to the original list
# of strings.
# The question here is if we convert a list of string to a single string, how will we know if a new string has started?
# We can use join and split using any delimeter, but the challenge is that that delimeter can be one of the characters of the actual strings.
# So we figured out a way- we will first put length of string, then delimeter #, then the string itself. 
# eg: ['i', 'love', 'leetcode'] will become '1#i4#love8#leetcode' 
# So whenever we encounter a #, we will go back to the left get the integer before it, 
# and will forward to the right to get the word as we have the length of the word. 
# This will never fail.

# TC of encode and decode = O(n) where n is total number of characters in strs and s

class Codec:
    def encode(self, strs: List[str]) -> str:
      
      enRes = ''
      for s in strs: 
        enRes += str(len(s)) + '#' + s
      
      return enRes
    
    def decode(self, s: str) -> List[str]:
      
      deRes = []
      i = 0
      
      while i < len(s):
        j = i
        while s[j] != '#':
          j += 1
        len_word = int(s[i:j])
        deRes.append(s[j+1 : j+1+len_word])
        i = j + 1 + len_word
      return deRes

