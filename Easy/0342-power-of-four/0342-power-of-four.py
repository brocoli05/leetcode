class Solution:
    def isPowerOfFour(self, n: int) -> bool:        
        x = 0
        while n >= 4**x:
            if n == 4**x:
                return True
            x += 1
        return False