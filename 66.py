from typing import List
from utils.test import test
import os


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return [int(digit) for digit in str(int("".join(map(str, digits))) + 1)]
    

solution = Solution()

test_cases = [[1, 2, 3], [4,3,2,1], [9]]
test_results = [solution.plusOne(case) for case in test_cases]

results = [[1, 2, 4], [4, 3, 2, 2], [1, 0]]

test(os.path.basename(__file__), test_results, results)
