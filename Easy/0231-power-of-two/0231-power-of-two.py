class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        elif n == 1:
            return True
        elif n % 2 == 0:
            n /= 2
            return self.isPowerOfTwo(n)
        else:
            return False