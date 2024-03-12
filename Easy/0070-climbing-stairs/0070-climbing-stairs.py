class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Method 1) Memorization
        """
        lst = [None] * (n + 1)
        
        def climbStairs_recursive(i):
            if i <= 2:
                return i
            elif lst[i] is not None:
                return lst[i]
            else:
                res = climbStairs_recursive(i-1) + climbStairs_recursive(i-2)
                lst[i] = res
            return res
        
        return climbStairs_recursive(n)
        
        """
        Method 2) Dynamic Programming
        """
#         if n <= 2:
#             return n
#         elif n < 0:
#             return
#         else:
#             lst = [None]*(n+1)
#             lst[0] = 1
#             lst[1] = 1
#             lst[2] = 2
            
#             for i in range(3, n + 1):
#                 lst[i] = lst[i - 1] + lst[i - 2]
                
#             return lst[n]