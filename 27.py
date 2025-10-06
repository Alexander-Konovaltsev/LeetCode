from typing import List
from utils.test import test
import os


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == val:
                del nums[i]

        return len(nums)
    

solution = Solution()

test_cases = [[[3,2,2,3], 3], [[0,1,2,2,3,0,4,2], 2]]
test_results = [solution.removeElement(case[0], case[1]) for case in test_cases]

results = [2, 5]

test(os.path.basename(__file__), test_results, results)
