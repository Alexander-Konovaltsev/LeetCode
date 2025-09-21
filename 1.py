from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_idxes = {}

        for idx, num in enumerate(nums):
            diff = target - num

            if diff in nums_idxes:
                return [nums_idxes[diff], idx]
            
            nums_idxes[num] = idx
            
        return []
    
sol = Solution()

test_cases = [[[2, 7, 11, 15], 9], [[3, 2, 4], 6], [[3, 3], 6]]

for case in test_cases:
    print(sol.twoSum(case[0], case[1]))
    