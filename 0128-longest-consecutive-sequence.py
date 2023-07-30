# Sorting:
# We can sort the entire array, and just keep checking neighbouring elements if they are consecutive. If so, it's a sequence, 
# else a new sequence has started.

# TC = O(nlogn) as sorting is nlogn
# SC = O(1) as sorting might be considered in-place, so no new data structure is created

----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# NEETCODE Best solution:
# Draw a numberline and plot the elements on it. We see that consecutive elements would be forming a group(sequence) that would be 
# separate from other groups/elements.
# We see that there are multiple sequences. We just need to see if a sequence has started, and how long it is.
# In order to know if a sequence has started, we take element n and check in set if we have it's left neighbour= n-1 in the array. 
# If not, that element n starts a sequence. Now since the sequence has started, check if we have n+1, n+2, n+3, etc. and keep 
# incrementing count.
# To achieve this, we just need to add current length of sequence to n, and it will keep going till that sequence is over.
# Longest sequence will be maximum of longest and length of current sequence. This variable is updated after each sequence. 
# Length of sequence is set to 0 when a sequence starter is encountered

# TC =  O(n) (linear time solution- we are iterating through array and expanding each range- so we will be visting an element 
# at most twice)  
# SC = O(n) (linear space solution)- we are creating a set

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
      
      numsSet = set(nums)
      
      longest = 0
      
      for n in nums:
        if (n-1) not in numsSet:
          length_seq = 0
          while (n + length_seq) in numsSet:
            length_seq += 1
          
          longest = max(longest, length_seq)
          
      return longest
    
------------------------------------------------------------------------------------------------------------------------------------------------------------------------
