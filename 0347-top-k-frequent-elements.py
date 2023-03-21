# Create a hashmap to count the number of occurences of elements(keys). Sort the hashmap in ascending order- nlogn

# TC = O(nlogn)
# SC = O(n)

--------------------------------------------------------------------------------------------------------------------------------------------------------------------

# But we do not want to sort the entire hashmap, but only k values as we need only k elements. This can be done using heap- create a max heap
# The key for this max heap will be number of occurences, and then we pop from heap exactly k times.

# TC = initializing heap and add the entire set of hashmap, it's going to be O(n) using heapify(), popping from the heap k times, each pop is O(logn) = O(klogn)
# SC = O(n)

# *as far as k < n, O(klogn) would be better than O(nlogn)

-------------------------------------------------------------------------------------------------------------------------------------------------------------------


# NEETCODE Best Solution:
# Here, the idea is to create a hash map- count. count will contain nums as keys, and their count as values.
# We create another list called freq which has empty lists. We'll be using this for bucket sort.
# For this list, values from count will act as indices, and keys from count will be the value of elements.
# Since there can be more than 1 value at an index(because, for example, frequency of 100 is 2, and 200 is also 2), we use list[100, 200] to capture all the elements 
# (which has frequency 2.)
# Then we go from right to left into the freq list, as we need k elements with highest frequency
# As soon as we get the k elements, we return the list

# TC = O(n) (max size of the freq array is equal to len(nums) = n, and at freq[p], worst case, all n elements are distinct in nums, so
# we are going to iterate at one element of array freq n times, n + n = 2n ~ n ) 
# SC = O(n) (creating hashmap count, and array freq) 



class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
      
      count = {}
      freq = [[] for x in range(len(nums)+1)] 
      res = []
      
      for i in nums:
        count[i] = 1 + count.get(i, 0)
        
      for n, c in count.items():
        freq[c].append(n)
        
      for p in range(len(nums)-1, -1, -1):
        for q in freq[p]:
          res.append(q)
          if len(res) == k:
            return res
          
----------------------------------------------------------------------------------------------------------------------------------------------------------------------



          
