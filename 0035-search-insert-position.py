# Approach 1:
# THIS APPROACH DOESN'T WORK- WE CAN DO BETTER USING BINARY SEARCH

# Use a for loop to find the index of the target. 
# If target is not present, return the index of element just larger than the target.
# If all the elements are smaller than target, then the predicted positin will be the end of the array, so return length of array

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
       
        for c in range(len(nums)):
            if nums[c] >= target:
                return c

        return len(nums)

# TC = O(n)- iterating through each element
# SC = O(1)- not using extra space

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# NEETCODE Best Solution:
# We want to solve this in O(logn) time, not in O(n) time. So we'll do binary search.
# Start by creating 2 pointers- `start` and `end` at the first and last element of the array because at this time, we are considering entire array. 
# `middle` pointer will be at (start+end)//2 position. Comapre element at the middle pointer and target. If 
#   target < nums[middle] --> we need to search left part of the array --> make end pointer = middle-1
#   target > nums[middle] --> we need to search right array --> make start pointer = middle+1
# keep comparing target and element at middle pointer till we finally find the target. Return middle. 

# now the question is to return the position of the target IF it was in the array
# after each execution of the loop, the array is halved, and we get closer to the position of the target
# at the last execution, `start`, `end` and `middle` will be poining at the same element, or would be very close to one another.
#   target < nums[middle] --> we need to search left part of the array --> make end pointer = middle-1 --> 
#     so `end` will be in the left of `start` which breaks while loop, so return `middle` or `start`
#   target > nums[middle] --> we need to search right array --> make start pointer = middle+1 --> 
#     `start` will be in the right of `end` which breaks the while loop, so return `middle + 1` or `start`

# Time Complexity = O(logn)- with each loop executed, the size of the array we search is halved
# Space Complexity = O(1)- no extra space used

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
       
        start = 0
        end = len(nums)-1

        while start <= end:
            middle = (start+end)//2

            if target < nums[middle]:
                end = middle - 1
            elif target > nums[middle]:
                start = middle + 1
            else:
                return middle

        return start
    #   return middle if target < nums[middle] else middle + 1

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

