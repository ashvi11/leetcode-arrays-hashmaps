
# NEETCODE Best Solution
# Create a new array and push elements from nums- how many time? To answer that, we wrapped it in a for loop and kept range to 2.
# If interviewer asks to do this 100 time, we just need to change range to 100- MOST EXTENSIBLE SOLUTION. es of elements(keys).

# TC = O(n)~ 2n- pushing 1 element in the new array takes O(1) time, here we are pushing 2n elements
# SC = O(n)~ 2n- we created a new array with length 2n, but since it was required in question, we can also think of it as O(1)

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        ans = []
        for i in range(2):
            for j in nums:
                ans.append(j)
        return ans

--------------------------------------------------------------------------------------------------------------------------------------------
# Approach 2: Simple 1 line code

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        ans = nums*2
        return ans

# TC = O(n)- read explanation above
# SC = O(n)- read explanation above


--------------------------------------------------------------------------------------------------------------------------------------------

# Approach 3: My solution- not creating a new array- well this is wrong because questions asks us to create a new array- but this
# could be asked as Follow-up

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        len_nums = len(nums)
        for i in nums:
            if len(nums) < len_nums*2:
                nums.append(i)
        
        return nums

# TC = O(n)- read explanation above
# SC = O(1)- no new array created

-------------------------------------------------------------------------------------------------------------------------------------------
