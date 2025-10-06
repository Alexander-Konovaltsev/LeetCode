from typing import List
from utils.test import test
import os


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        nums_count = {}
        for num in nums:
            nums_count[num] = nums_count.get(num, 0) + 1

        max_frequency = max(list(nums_count.values()))
        nums_with_max_frequency = 0
        
        for val in nums_count.values():
            if val == max_frequency:
                nums_with_max_frequency += 1

        return nums_with_max_frequency * max_frequency
    

solution = Solution() 

test_cases = [[1,2,2,3,1,4], [1,2,3,4,5]]
test_results = [solution.maxFrequencyElements(case) for case in test_cases]

results = [4, 5]

test(os.path.basename(__file__), test_results, results)
