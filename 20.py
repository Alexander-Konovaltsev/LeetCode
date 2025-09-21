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

sol = Solution()

test_cases = ["()", "()[]{}", "(]", "([])", "([)]"]

for case in test_cases:
    print(sol.isValid(case))