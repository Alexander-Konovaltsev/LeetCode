from utils.test import test
import os


class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        
        stack = []
        bracket_pairs = {')': '(', ']': '[', '}': '{'}

        for bracket in s:
            if bracket in bracket_pairs.values():
                stack.append(bracket)
                continue

            if not stack or stack.pop() != bracket_pairs[bracket]:
                return False
        
        return not stack


solution = Solution()

test_cases = ["()", "()[]{}", "(]", "([])", "([)]"]
test_results = [solution.isValid(case) for case in test_cases]

results = [True, True, False, True, False]

test(os.path.basename(__file__), test_results, results)
