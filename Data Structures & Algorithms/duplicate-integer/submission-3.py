class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for index, num in enumerate(nums):
            if num in hashset:
                return True
            hashset.add(num)
        return False
        