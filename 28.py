from utils.test import test
import os


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
    

solution = Solution()

test_cases = [["sadbutsad", "sad"], ["leetcode", "leeto"]]
test_results = [solution.strStr(case[0], case[1]) for case in test_cases]

results = [0, -1]

test(os.path.basename(__file__), test_results, results)
    