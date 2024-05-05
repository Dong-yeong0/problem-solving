from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # ! Solution 1
        # freq_dict = {}
        # for num in nums:
        #     if num in freq_dict:
        #         freq_dict[num] += 1
        #     else:
        #         freq_dict[num] = 1

        # max_value = 0
        # most_freq_element = None

        # for key, value in freq_dict.items():
        #     if value > max_value:
        #         max_value = value
        #         most_freq_element = key

        # return most_freq_element 
        
        # ! Solution 2
        # cnt = {}
        # n = len(nums)
        # for num in nums:
        #     if num not in cnt:
        #         cnt[num] = 0
        #     cnt[num] += 1
            
        #     if cnt[num] > n // 2 :
        #         return num
        
        # ! Solution 3
        # from collections import Counter
        # counter = Counter(nums)
        # most_common_element, freq = counter.most_common(1)[0]
        # return most_common_element
        
        # ! Solution 4
        nums.sort()
        return nums[len(nums) // 2]
        

# nums = [2,2,1,1,1,2,2]
nums = [3,2,3]
solution = Solution()
print(solution.majorityElement(nums))