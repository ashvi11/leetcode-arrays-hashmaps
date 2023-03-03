# 1- Brute Force- take 1 element of the array and add it with other elements, and check if it matches the target. Do it with every element that comes after the checked
# one.
# TC = O(n^2)
# SC = O(1)

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 2 NEETCODE Best Approach- Create an empty hashmap(dictionary). Keys will be elements, values will be their indices. So use enumerate to start from 0 to upto n. 1st
# variable for enumerate will be 0, 1, etc, 2nd variable will be value of element.
# Calculate diff. If difference already not in the hashmap, add out current (i, n). If difference already in the hashmap, output incex of diff and i(index of current
# element.
# With this code, eg: nums [2, 4, 5, 1], target = 5. So till now, 3(5-2 = 3) is not in the hashmap, so (2, 0) will be added to the hashmap. Then 1(5-4 = 1) is not in
# the hashmap, so (4,1) will be added. Then 0(5-5 = 0) is not yet in the hashmap, so (5, 2) will be added. Then 4(5-1 = 4) is already in the hashmap, so 
# index of 4(1) and i(3) will be returned.

# TC = O(n) (itereating through array = n, adding n elements to hashmap = n, checking if a value exists in the hashmap = n, n+n+n = 3n ~ n)
# SC = O(n) (as we can potentially add all elements or n-1 elements to the hashmap ~ n)


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      
      prevMap = {}
      
      for i, n in enumerate(nums):
        diff = target - n
        if diff in prevMap:
          return [prevMap[diff], i]
        prevMap[n] = i
      
      return
    
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
