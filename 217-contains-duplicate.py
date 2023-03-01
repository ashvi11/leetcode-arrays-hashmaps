# 1
# Worst approach- Brute Force- compare 1 item of array to all other items. Do this for all elements of array. Since we would be using for loop twice:
# TC = O(n^2)
# SC = O(1) (we are not creating another array)


# 2
# 2nd best approach- sort the array, so we will only compare neighbouring elements. Do this for all elements of array.
# TC = O(nlogn) (n for all elements, log n for sorting)
# SC = O(1)  (we are not creating another array)

#3
# Best approach for time complexity- create a hashset. If an element is not present in the hashset, add it. If already present, return True

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
      seen = set()
      
      for i in nums:
        if i in seen:
          return True
        seen.add(i)
     return False


