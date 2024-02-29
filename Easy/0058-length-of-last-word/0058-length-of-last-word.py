class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        max_len = 0
        word_len = 0
        
        for ch in s:
            if ch != ' ':
                word_len += 1
            else:
                if word_len > 0:
                    max_len = word_len
                word_len = 0
                
        # for last word
        if word_len > 0:
            max_len = word_len
            
        return max_len