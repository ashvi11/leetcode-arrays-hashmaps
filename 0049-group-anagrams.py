#1 Sort each string in the list. Hence, after sorting, anagrams will become equivalent strings.

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = defaultdict(list)

        for s in strs:
            sorted_s = sorted(s)
            sorted_s_str = ''.join(sorted_s)

            for sorted_s_str in res:
                res[sorted_s_str].append(s)
            else:
                res[sorted_s_str] = [s]

        return res.values()



#TC = O(m*nlogn) where n is average length of each string(sorting n = nlogn), and m is length of the list(doing nlogn m times)   



#1 NEETCODE Best approach:
# all characters in all the strings in the list are going to be from a to z, i.e. 26 characters. Let's initate an array count. This will keep a track of count of
# letters in a string, for all strings in the list: eg for 'bat', count = [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]- 1 for a at
# count[0], 1 for b at count[1], and 1 for t at count[19]. This count will be our key, and values will be list of strings that has similar list.
# defaultdict() creates a dictionary with values = [](empty list).
# As list cannot be key, we will convert it to a tuple, and append 'bat' string, (s in this case) to that empty list of strings.
# ord(c) - ord('a') - this gives tells us which index to add 1. E.g.: ascii value of 'a' = 65, and 'b' = 66. If c(in code) = 'b', c = 66. Hence 66 - 65 = 1.
# This gave us that at index 1, add 1- really smart solution.

# TC = O(m*n) (O(m*n*26) ~ O(m*n))  m = number of strings in input array, n =  average length of each string, 26 = length of count array)
# SC = O(m) (O(m*26) ~ O(m)- we are creating count array 26 times and a hashmap)



class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
      
      res = defaultdict(list)
      
      for s in strs:
        count = [0] * 26
        
        for c in s:
          count[ord(c) - ord('a')] += 1
          
          res[tuple(count)].append(s)
          
        return res.values()
