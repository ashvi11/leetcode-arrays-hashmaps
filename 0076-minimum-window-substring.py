# The concept is to take a substring, and expand from right if all characters and their count match with t. 
# Once it matches with t, shrink the window from the left because we want string with min length.
# How can we determine if our current window contains all characters of t without iterating through the entire hashmap?
# By keeping track of 2 variables- the total number of unique characters we have from `t` in our current window and total number of
# unique characters we need from 't'- have, need variables from code
# Each time we add a character to our window that makes the count of that character match what's needed in `t`, we increment `have`. 
# We know our window contains all characters of `t` when `have` equals `need`

# first, handle edge case
# then we'll create a hashmap `countT` which will store count of characters in t- this is what we need. `need` will store count of unique
# characters in `countT` hashmap
# declare other variables- `l`', `res`, `resLen`, `have`, `need`- `res` has to be 2 values- l and r- we pack these in a list. 
# This is because we need to retrieve l and r at the end to return the min length string. `resLen` will keep track of min len string
# currently resLen = infinity because we want min len, and we are guaranteed to have at least one solution < infinity
# now we iterate through s, create a hashmap `window` to keep track of count in the current window.
# we don't care about the elements not in t. if count of that new element `c` in window matches count of `c` in countT, we can conclude
# that we have correct count of c that we needed, so increment have.
# Keep expanding the substring till we get all unique characters in window that we needed from t. Now have == need
# Once have == need, now we check the length of this substring- is this less then current resLen? If no, move ahead- explained shortly
# if length of this substring is less then current resLen, update `resLen` to this length. update `res` to this l and r
# this is because uptil this point, this is the min length string that we found
# Back to problem- next step will be to shrink window from left.
# First decrement the value of current count of l in `window` hashmap- if this is the element not in t, we don't care
# if current left `s[l]` is in t, and decrementing it from `window` makes it less than it's count in countT, it means that now we are
# short of a character, and that have < need. So decrement have by 1
# increment l pointer in any case
# Expand substring if have != need, shrink substring if have == need- do this till we reach the end of the string
# Once we reach there, our current resLen will the the resultant length and `res` will be the final result. Assign this to l and r
# Retrieve the string using this l and r if resLen != infinity, else return ""


# TC = O(n + m) where n is length of s and m is length of t, as we go through both s and t once.
# SC = O(1)- because the hashmaps can be at most size O(52) because only uppercase and lowercase alphabets are going to be in s and t
# So at most the size will be O(52) and it will not grow with the size of the strings

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if t == " ":
            return " "

        window, countT = {}, {}

        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        
        l = 0
        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("infinity")

        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)
        
            if c in countT and window[c] == countT[c]:
                have += 1
            
            while have == need:
                if (r-l+1) < resLen:
                    res = [l, r]
                    resLen = r-l+1
                
                window[s[l]] -= 1

                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                
                l += 1
        l, r = res
        return s[l:r+1] if resLen != float("infinity") else ""
      
---------------------------------------------------------------------------------------------------------------------------------------
