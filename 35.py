from typing import List
from utils.test import test
import os


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return left
    

solution = Solution()

test_case = [1, 3, 5, 6]
test_cases = [[test_case, 5],[test_case, 2], [test_case, 7]]
test_results = [solution.searchInsert(case[0], case[1]) for case in test_cases]

results = [2, 1, 4]

test(os.path.basename(__file__), test_results, results)
    