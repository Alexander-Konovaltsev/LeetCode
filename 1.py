from typing import List
from utils.test import test
import os


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_idxes = {}

        for idx, num in enumerate(nums):
            diff = target - num

            if diff in nums_idxes:
                return [nums_idxes[diff], idx]
            
            nums_idxes[num] = idx
            
        return []
    

solution = Solution()

test_cases = [[[2, 7, 11, 15], 9], [[3, 2, 4], 6], [[3, 3], 6]]
test_results = [solution.twoSum(case[0], case[1]) for case in test_cases]

results = [[0, 1], [1, 2], [0, 1]]

test(os.path.basename(__file__), test_results, results)
    