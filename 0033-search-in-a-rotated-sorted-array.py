# NEETCODE Best Solution but longer code:

# Rotated array can be seens as a singlle array broken from a pivot point and the two parts are swapped.
# So there's a left sorted array(LSA) and a right sorted array(RSA).
# First we calclate m using l and r. Then look for where is m? LSA or RSA?
# m in LSA:
#   t > nums[m]- this means target is higher, so it won't be in RSA, or on left side of LSA, so search right(in LSA)
#   t < nums[m]- this means target is lower, so it could be either in RSA or on left side in LSA 
#     t < nums[l]- this means target is lower than the current nums[l], so it's in RSA- search right in RSA
#     t > nums[l]- this means target is between l and m, so it's in LSA, so search left in LSA
# m is in RSA:
#   t < nums[m]- this means target is lower than current m, so it won't be in LSA(because elements in LSA are higher than in RSA),
#   so it will be in RSA, so search left in RSA
#   t > nums[m]- this means target is higher, so it could be either in LSA or RSA
#     t > nums[r]- greater than the current nums[r], so it's in LSA, so search left
#     t < nums[r]- between nums[m] and nums[r], so search right in RSA
# at some point target will be  == nums[m]- return m, else return -1

# Time Complexity = O(logn)
# Space Complexity = O(1)

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if target == nums[m]:
                return m

            if nums[l] <= nums[m]:
                # m is in left sorted array
                if target > nums[m]:
                    # look on right side in LSA
                    l = m + 1
                else:
                    if nums[l] > target:
                        # look on right side in RSA
                        l = m + 1
                    else:
                        # look on left side in LSA
                        r = m - 1
                
            else:
                # m is in right sorted array
                if target < nums[m]:
                    # look on left in RSA
                    r = m - 1
                else:
                    if target > nums[r]:
                        # look on left in LSA
                        r = m - 1
                    else:
                        # look on right side in RSA
                        l = m + 1
        return -1

---------------------------------------------------------------------------------------------------------------------------------

# NEETCODE Neat-code:

# Same logic and TC, SC as above, only the code is smaller adn neater.

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if target == nums[m]:
                return m

            if nums[l] <= nums[m]:
                # m is in left sorted array
                if target > nums[m] or nums[l] > target:
                    # serch right side in LSA or search right side in RSA
                    l = m + 1
                else:
                    # search left side in LSA
                    r = m - 1
                
            else:
                # m is in right sorted array
                if target < nums[m] or target > nums[r]:
                    # search left in RSA or search left in RSA
                    r = m - 1
                else:
                    # search right side in RSA
                    l = m + 1
        return -1

---------------------------------------------------------------------------------------------------------------------------------

