class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]
    

sol = Solution()

test_cases = [["11", "1"], ["1010", "1011"]]

for case in test_cases:
    print(sol.addBinary(case[0], case[1]))
