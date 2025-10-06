from typing import List
from utils.test import test
import os


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs_lens = [len(s) for s in strs]
        common_prefix = ""

        if min(strs_lens) == 0:
            return common_prefix
        
        for i in range(min(strs_lens)):
            current_syms = [s[i] for s in strs]
            if len(set(current_syms)) != 1:
                break          
            common_prefix += current_syms[0]
            
        return common_prefix
    

solution = Solution()

test_cases = [["flower", "flow", "flight"], ["dog", "racecar", "car"]]
test_results = [solution.longestCommonPrefix(case) for case in test_cases]

results = ["fl", ""]

test(os.path.basename(__file__), test_results, results)
