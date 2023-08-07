# Take two pointers l and r- s[l:r+1] will be the substring. Increment r no matter what.
# We take a substring, and find which char has the max count. We won't replace that character, but characters other than that. 
# So we do diff = len(substring)-count of max char. Eg: len = 8, max char count = 6, so diff = 8 - 6 = 2. So 2 characters are replacable. 
# Now compare diff with k. If diff <= k, res = len of string and increment r. If diff > k, it means there are more characters to replace than it's allowed. 
# So in this case, increment l pointer. Now we are not considering element at previous l, so decrement count of that previous l from hashmap. Do this until diff <= k 
# Keep updating a longest variable- it will be max of length of substrings. 
# Return longest

# TC = O(n) ~ O(26.n) because worst case we have all 26 characters- uppercase A to uppercase Z. Question says s will only have uppercase characters
# SC = O(n)- creating a hashset

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        longest = 0
        freq = {}

        for r in range(len(s)):
            freq[s[r]] = 1 + freq.get(s[r], 0)
            # max_char = max(freq.values())
            # diff = (r-l+1) - max(freq.values())
            # res = r-l+1
            while r-l+1 - max(freq.values()) > k:
                freq[s[l]] -= 1
                l += 1
                
            longest = max(longest, r-l+1)
        return longest

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
