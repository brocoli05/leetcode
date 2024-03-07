class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if len(digits) == 1:
            return [digits[0] + 1] if digits[0] < 9 else [1, 0]
        else:
            sum_digits = 1
            
            for i in range(len(digits)):
                sum_digits += digits[i] * (10 ** (len(digits) - 1 - i))

            new_digits = [int(digit) for digit in str(sum_digits)]
            
            return new_digits
        