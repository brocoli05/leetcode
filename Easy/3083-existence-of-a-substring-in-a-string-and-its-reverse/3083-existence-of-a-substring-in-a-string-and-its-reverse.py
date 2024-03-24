class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        # reverse string
        revSubstring = s[::-1]
        for i in range(len(s)-1):
            # create substring of length 2
            substring = s[i] + s[i+1]
            # compare with original substring
            if substring in revSubstring:
                return True
            
        return False
            
        
        