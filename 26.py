from typing import List
from utils.test import test
import os


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique_nums = sorted(set(nums))

        for idx, num in enumerate(unique_nums):
            nums[idx] = num

        return len(unique_nums)
    

solution = Solution()

test_cases = [[1,1,2], [0,0,1,1,1,2,2,3,3,4], [-1,0,0,0,0,3,3]]
test_results = [solution.removeDuplicates(case) for case in test_cases]

results = [2, 5, 3]

test(os.path.basename(__file__), test_results, results)
