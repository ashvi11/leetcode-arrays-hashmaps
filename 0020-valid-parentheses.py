# NEETCODE Best Approach:
# We'll use STACK for this question- stack.pop() eliminates the last element from the stack, this is what we want.
# Create a hashmap, where closing bracket will be the key and opening bracket will be value- for all types of brackets allowed like {']':'['} 
# Start iterating through stack- let's say current element is c.
# Check if c is opening brakcet or closing:  
#   if it's closing bracket, the stack shouldn't be empty, and the last element of the stack should be it's corresponding opening bracket.
#   If these conditions are met, pop the last element from the stack, iterate the next element. If not met, return False immediately
# If c is an opening bracket, append it to the stack.
# At the end, return True if stack is empty, else return False

# TC = O(n)-  we are iterating through all chatacters of the string once
# SC = O(n)- worst case- there would be n characters in the stack

class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        closeToOpen = {']':'[', ')':'(', '}':'{'}

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else: 
                    return False
            else: 
                stack.append(c)

        return True if not stack else False

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
