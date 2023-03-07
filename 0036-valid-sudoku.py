# NEETCODE Best Solution-
# here the concept is not to check if there is only one number at an empty space on the board- if there are multiple possible numbers, the board is invalid-
# THE ABOVE IS NOT THE CONCEPT, so we don't have to worry about that
# The concept is to check if there are no duplicates in rows, columns and 3x3 squares
# we use hashmap- for rows and columns, 0-9 would be key, and the set will be the value. Set contains all elements in that row and column respectively.
# for squares, we would use hashmap as well, but the keys would be a row and column index pair (row/3, col/3)- this would be a tuple as key cannot be list.
# for squares, for row and column index is divided by 3, so we know which square are we talking about- eg if on real board it's 0x4, in mapped version it 
# would be 0x1. So we are looking at the top-middle square.
# for the code- iterate through the matrix(nested list- r represents innner list, c represents elements of inner list). If we encounter ".", go ahead
# if we encounter a number, check if that number is already present in all 3 hashmaps. If so, return False immediately
# If not present already, add them to the set. If False is not returned at all, return True

# TC = O(9^2) as we are iterating over the entire 9x9 grid once
# SC = O(9^2) we are going to have 3 hashsets exactly 9^2 size (in rows, 9 keys, each key has 9 values worst case, same for cols and sqrs)



class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
      
      rows = collections.defaultdict(set)
      cols = collections.defaultdict(set)
      sqrs = collections.defaultdict(set)
      
      for r in range(9):
        for c in range(9):
          if board[r][c] == '.':
            continue
          
          if (board[r][c] in rows[r] or
             board[r][c] in cols[c] or
             board[r][c] in sqrs[(r//3, c//3)]):
            return False
          
          rows[r].add(board[r][c])
          cols[c].add(board[r][c])
          sqrs[(r//3, c//3)].add(board[r][c])
       
      return True

---------------------------------------------------------------------------------------------------------------------------------------------------------------------
            
       
