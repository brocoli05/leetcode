class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0:
            return True
        else:
            new_s = [c.lower() for c in s if c.isalnum()]
           
            # Check if the filtered string is a palindrome
            left, right = 0, len(new_s) - 1
            while left < right:
                if new_s[left] != new_s[right]:
                    return False
                left += 1
                right -= 1
            return True
            # mid = len(new_s)//2
            # for i in range(mid):
            #     j = len(new_s) -i -1
            #     if new_s[i] != new_s[j]:
            #         return False
            # return True        
            