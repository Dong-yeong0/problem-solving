class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        cnt = 0
        for num in nums:
            if num != val:
               nums[cnt] = num 
               cnt += 1  
        
        return cnt