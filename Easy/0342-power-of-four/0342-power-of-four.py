class Solution:
    def isPowerOfFour(self, n: int) -> bool:        
        ## using recursion       
        if n == 1:   # check the base case
            return True
        elif n <= 0 or n % 4 != 0:
            return False
        else:
            return self.isPowerOfFour(n // 4)