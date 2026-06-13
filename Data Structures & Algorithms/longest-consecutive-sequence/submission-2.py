class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        nums.sort()
        longest_streak = 1
        current_streak = 1
        for i in range(len(nums) - 1):
            if nums[i + 1] == nums[i]:
                continue
            elif nums[i + 1] - nums[i] == 1:
                current_streak += 1
                continue
            else:
                longest_streak = max(longest_streak, current_streak)
                current_streak = 1
            
        return max(longest_streak, current_streak)



        