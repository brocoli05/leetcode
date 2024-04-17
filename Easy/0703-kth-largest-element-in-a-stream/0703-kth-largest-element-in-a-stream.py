class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.sorted_nums = []
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        # insert val into sorted_nums
        i = 0
        while i < len(self.sorted_nums) and self.sorted_nums[i] <= val:
            i += 1
        self.sorted_nums.insert(i, val)
        # trim the list to contain only the k largest elements
        if len(self.sorted_nums) > self.k:
            self.sorted_nums.pop(0)
        # return the kth largest element
        return self.sorted_nums[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)