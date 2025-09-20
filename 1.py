from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx_1, num_1 in enumerate(nums):
            for idx_2, num_2 in enumerate(nums):

                if idx_1 == idx_2:
                    continue
                if (num_1 + num_2) == target:
                    return [idx_1, idx_2]
                        
        return [0]
    
sol = Solution()

test_cases = [ [[2, 7, 11, 15], 9], [[3, 2, 4], 6], [[3, 3], 6]]

for case in test_cases:
    print(sol.twoSum(case[0], case[1]))
    