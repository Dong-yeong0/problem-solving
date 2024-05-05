from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = j = 1
        for i in range(i, len(nums)):
            if nums[i] != nums[i-1]:
                nums[j] = nums[i]
                j += 1
        return j

nums = [1,1,2]
print(Solution.removeDuplicates(nums))