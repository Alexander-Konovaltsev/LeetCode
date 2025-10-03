class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])
    

sol = Solution()

test_cases = ["Hello World", "   fly me   to   the moon  ", "luffy is still joyboy"]

for case in test_cases:
    print(sol.lengthOfLastWord(case))
