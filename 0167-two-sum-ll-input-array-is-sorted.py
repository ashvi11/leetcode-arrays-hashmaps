# Brute Force:
# add i(first) element to the j(i+1) element If sum < target, keep incrementing j. When sum > target, eliminate curr j and remainder of the array,because the
# array is sorted, so sum of i and any element after current j would be greater than target anyway.
# Do this for all elements.

#TC = O(n^2)
#SC = O(1)

----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# NEETCODE Best solution:
# initiate two pointers- left(l) and right(r)- l at 0th index, r at the len(nums)-1 index. Now add these two- if the total is > target, the number is too big.
# So, since the array is sorted, if we add l+1 to r it will be anyway greater than target. So we will keep l as it is and decrement r.
# if the total  target, numbers are too small. So we need to increment l. This way by moving the two pointers, we will get our solution since it is guaranteed.
# We have to output index starting at 1 instead of 0, so we will add 1 to l and r in the output.

# TC = O(n) as we are iterating entire array(or less if we get solution early) once
# SC = O(1) as we are not creating any other data structured

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
      
      l = 0
      r = len(numbers)-1
      
      while l < r:
        if numbers[l] + numbers[r] > target:
          r -= 1
        elif numbers[l] + numbers[r] < target:
          l += 1
         else:
          return [l+1, r+1]
       return []
    
----------------------------------------------------------------------------------------------------------------------------------------------------------------------
