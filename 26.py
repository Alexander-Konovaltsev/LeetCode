from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique_nums = sorted(set(nums))

        for idx, num in enumerate(unique_nums):
            nums[idx] = num

        return len(unique_nums)
    
sol = Solution()

test_cases = [[1,1,2], [0,0,1,1,1,2,2,3,3,4], [-1,0,0,0,0,3,3]]

for case in test_cases:
    print(sol.removeDuplicates(case), case)
