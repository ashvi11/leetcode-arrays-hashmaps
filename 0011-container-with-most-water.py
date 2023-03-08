# Brute Force:
# Compare each height element with other height element to find the area

# TC = O(n^2)
# SC = O(1)

class Solution:
    def maxArea(self, height: List[int]) -> int:
      
      max_area = 0
      for l in range(len(nums)-1):
        for r in range(l+1, len(nums)-1):
          area = (r-l) * min(height[l], height[r])
          max_area = max(area, max_area)
          
       return max_area 
    
----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# NEETCODE Best Solution:
# The concept here is to pick the min number, because if we pick the max number, the water will spill. That will be height. The width will be r-l
# Initiate two pointers- l, r. Calculate the area. Update Max_Area variable. Whichever side is minimum will move forward. This way, we will keep moving, calculating
# new area and updating Max_Area. 
# This will guatantee the answer, as we are moving forward from min sides.

# TC = O(n) linear time solution
# SC = O(1)

class Solution:
    def maxArea(self, height: List[int]) -> int:
      
      maxArea = 0
      l = 0
      r = len(height)-1
      
      while l < r:
        area = (r-l) * min(height[l], height[r])
        maxArea = max(maxArea, area)
        
        if height[l] < height[r]:
          l += 1
        else:
          r -= 1
          
      return maxArea

 ---------------------------------------------------------------------------------------------------------------------------------------------------------------------
