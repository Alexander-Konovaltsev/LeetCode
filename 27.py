from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == val:
                del nums[i]

        return len(nums)
    
sol = Solution()

test_cases = [[[3,2,2,3], 3], [[0,1,2,2,3,0,4,2], 2]]

for case in test_cases:
    print(sol.removeElement(case[0], case[1]), case)