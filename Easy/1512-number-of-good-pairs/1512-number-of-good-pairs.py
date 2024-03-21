class Solution:
    class HashTable:
        class Node:
            def __init__(self, key):
                self.key = key
                self.next = None
        def __init__(self, size):
            self.size = size
            self.table = [None] * size
            
        def _hash(self, key):
            return key % self.size
        
        def insert(self, key):
            index = self._hash(key)
            if self.table[index] is None:
                self.table[index] = self.Node(key)
            else:
                node = self.table[index]
                while node.next:
                    node = node.next
                node.next = self.Node(key)
        
        # counts the number of identical pairs in the hash table
        def count_pairs(self):
            total_pairs = 0
        
            for bucket in self.table:
                if bucket:
                    # traverse the linked list in the bucket and count the number of nodes in the list
                    count = 0
                    node = bucket
                    while node:
                        count += 1
                        node = node.next
                    total_pairs += count * (count - 1) // 2
            return total_pairs
                
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # creates HashTable with the size of max_num + 1
        max_num = max(nums)
        hash_table = self.HashTable(max_num + 1)
        
        for num in nums:
            hash_table.insert(num)
        
        return hash_table.count_pairs()
        
        
        
        """
        cnt = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    cnt += 1
            
        return cnt
        """
        
                    