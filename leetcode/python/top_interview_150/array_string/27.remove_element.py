from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        cnt = 0
        for num in nums:
            if num != val:
                nums[cnt] = num 
                cnt += 1  
        
        return cnt
    
nums = [3,2,2,3]
val = 3
print(Solution.removeElement(nums, val))