# Brute Force:
# for each value i, calculate profit with every other value j after it. Repeat this for all elements.

# TC = O(n^2) 
# SC = O(1)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        maxProfit = 0

        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                profit = prices[j] - prices[i]
                maxProfit = max(profit, maxProfit)

        return maxProfit
 
------------------------------------------------------------------------------------------------------------------------------------------------------------

# NEETCODE Best Solution
# Sliding Window Approach- It's like 2 pointers, but instead of moving on opposite direction, they move in the same direction. 
# Initialized 2 pointers, l and r. l should always be on the left of r, as we cannot buy after sell. Keep l as it is, and increment r. 
# If value at l < value at r, this means there is some profit and we calculate that. Then move r.
# If value at l > value at r, this means there is no profit, so we would skip the calculation. We keep incremeting r till we find value at r > value at l.
# When we find this, new l = r, and r += 1.

# TC = O(n)
# SC = O(1)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        max_profit = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_profit = max(profit, max_profit)
            else:
                l = r
            r += 1
         return max_profit
    
----------------------------------------------------------------------------------------------------------------------------------------------------------             
            

