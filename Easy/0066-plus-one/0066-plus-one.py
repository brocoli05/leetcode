class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = int(''.join(map(str,digits)))
        num += 1
        
        return [int (i) for i in str(num)]
    
    """
    [1,2,3]             digits                      int
    ['1', '2', '3']     map(str, digits)            str
    '123'               ''.join(map(str,digits))    str
    123                 num                         int
    124                 num += 1                    int
    ['1', '2', '4']     [int(i) for i in str(num)]  str
    """
    
## Method 2    
#         if len(digits) == 1:
#             return [digits[0] + 1] if digits[0] < 9 else [1, 0]
#         else:
#             sum_digits = 1
            
#             for i in range(len(digits)):
#                 sum_digits += digits[i] * (10 ** (len(digits) - 1 - i))

#             new_digits = [int(digit) for digit in str(sum_digits)]
            
#             return new_digits
        