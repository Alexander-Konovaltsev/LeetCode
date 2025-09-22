class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
    
sol = Solution()

test_cases = [["sadbutsad", "sad"], ["leetcode", "leeto"]]

for case in test_cases:
    print(sol.strStr(case[0], case[1]))
    