class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        new_list = [0]*(rowIndex + 1)
        new_list[0] = 1
        
        for i in range(1, rowIndex + 1):
            j = i
            while j > 0:
                new_list[j] += new_list[j - 1]
                j -= 1
            
        return new_list
            