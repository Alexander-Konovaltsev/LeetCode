from utils.test import test
import os


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]
    

solution = Solution()

test_cases = [["11", "1"], ["1010", "1011"]]
test_results = [solution.addBinary(case[0], case[1]) for case in test_cases]

results = ["100", "10101"]

test(os.path.basename(__file__), test_results, results)
