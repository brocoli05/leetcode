class Solution:
    def addBinary(self, a: str, b: str) -> str:
        len_a = len(a)
        len_b = len(b)
        
        if len_a >= len_b:
            len_max = len_a
        else:
            len_max = len_b
        
        new_num = ""
        carry = 0
        
        for i in range(1, len_max + 1):
            # Retrieve the i-th bit from the end
            bit_a = int(a[-i]) if i <= len_a else 0
            bit_b = int(b[-i]) if i <= len_b else 0
            
            total_sum = bit_a + bit_b + carry
            new_bit = total_sum % 2
            carry = total_sum // 2
            
            # Insert the new bit at the beginning of the result
            new_num = str(new_bit) + new_num
            
        if carry:
            new_num = '1' + new_num
        
        return new_num