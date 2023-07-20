# 1
# Worst approach- Brute Force- compare 1 item of array to all other items. Do this for all elements of array. For 1 element it would be n x 1 = n, for n elements it would be n x n = n^2. We are not
# creating a new array

# TC = O(n^2)
# SC = O(1) (we are not creating another array)

------------------------------------------------------------------------------------------------------------------------------------------------------

# 2
# 2nd best approach- sort the array, so we will only compare adjacent elements. So we go through array once once. Sorting does take nlogn time

# TC = O(nlogn) (for sorting)
# SC = O(1)  (we are not creating another array)

------------------------------------------------------------------------------------------------------------------------------------------------------

#3 Neetcode best solution
# Best approach for time complexity- create a hashset. If an element is not present in the hashset, add it. If already present, return True
# First see if it's in hashmap, then add it if not already present

# TC = O(n) (we are iterating only once)
# SC = O(n) (we are creating a new set)

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
      seen = set()
      
      for i in nums:
        if i in seen:
          return True
        seen.add(i)
     return False

------------------------------------------------------------------------------------------------------------------------------------------------------

#4 My solution
# Convert list to set, and compare length of list and set. Set will remove all duplicates. If the length of list != length of set, return True. 

# TC = O(n) (converting list to set)
# SC = O(n) (creating a new set)

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_set = set(nums)
        
        if len(nums) != len(nums_set):
            return True
        return False

------------------------------------------------------------------------------------------------------------------------------------------------------
