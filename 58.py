from utils.test import test
import os


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])
    

solution = Solution()

test_cases = ["Hello World", "   fly me   to   the moon  ", "luffy is still joyboy"]
test_results = [solution.lengthOfLastWord(case) for case in test_cases]

results = [5, 4, 6]

test(os.path.basename(__file__), test_results, results)
