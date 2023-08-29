# NEETCODE Best Solution:

# Create a variable `res` to store current min value. Set it to nums[0]
# If the array is sorted- answer is nums[l] because it will always be the min element.
# If the array is not sorted, it means there's a pivot. Array on the left of pivot = LSA(left sorted array) and to the right of pivot = RSA. 
# We'll calculate m and check if this m is at the lower element than res. If so, update res. If not, check where is m- LSA or RSA. 
# If m is in LSA, we'd need to search right because LSA will never have min element. If m is in RSA, we'd not want to go any more right, so search left
# After multiple iterations, either array will get sorted(so apply nums[l] logic) or res would have captured m when it was pointing the min element. 
# Return res

# Time Complexity = O(logn)
# Space Complexity = O(1)


class Solution:
    def findMin(self, nums: List[int]) -> int:

        l, r = 0, len(nums) - 1
        res = nums[l]

        while l <= r:
            if nums[l] < nums[r]:
                res = min(nums[l], res)
                break
            
            m = (l + r) // 2
            res = min(res, nums[m])

            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        
        return res

-------------------------------------------------------------------------------------------------------------------------------------------------------
