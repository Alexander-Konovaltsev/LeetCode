from utils.test import test
import os


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        ver1 = list(map(int, version1.split('.')))
        ver2 = list(map(int, version2.split('.')))
        
        max_len = max(len(ver1), len(ver2))

        for ver in [ver1, ver2]:
            self.addZeroes(ver, max_len)

        for i in range(max_len):
            if ver1[i] < ver2[i]:
                return -1
            elif ver1[i] > ver2[i]:
                return 1
            
        return 0


    def addZeroes(self, lst: list, length: int) -> None:
        if len(lst) >= length:
            return
        
        lst.extend([0] * (length - len(lst)))


solution = Solution()

test_cases = [["1.2", "1.10"], ["1.01", "1.001"], ["1.0", "1.0.0.0"]]
test_results = [solution.compareVersion(case[0], case[1]) for case in test_cases]

results = [-1, 0, 0]

test(os.path.basename(__file__), test_results, results)
