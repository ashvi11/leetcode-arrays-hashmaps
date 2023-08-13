# Approach 1:
# THIS APPROACH DOESN'T WORK- QUESTION ITESELF STATES TO USE BINARY SEARCH

# Use a for loop to find the index of the target. If target is not present, return -1

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        for c in range(len(nums)):
            if nums[c] == target:
                return c
        return -1

# TC = O(n)- iterating through each element
# SC = O(1)- not using extra space

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# NEETCODE Best Solution:
# We want to solve this in O(logn) time, not in O(n) time. Sp we'll do binary search.
# Start by creating 2 pointers- `start` and `end` at the first and last element of the array because at this time, we are considering entire array. 
# `middle` pointer will be at (start+end)//2 position. Comapre element at the middle pointer and target. If 
#   target < nums[middle] --> we need to search left part of the array --> make end pointer = middle-1
#   target > nums[middle] --> we need to search right array --> make start pointer = middle+1
# keep comparing target and element at middle pointer till we finally find the target. Return middle. If target not found, return -1

# Time Complexity = O(logn)- with each loop executed, the size of the array we search is halved
# Space Complexity = O(1)- no extra space used

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
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

        return -1

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
