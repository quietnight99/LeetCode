from typing import List, Tuple

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1,len(nums)) :
                if nums[i] + nums[j] == target:
                    print(i,j)
                    return [i, j]

# 使用示例
res = Solution().twoSum(nums=[4, 7, 11, 1], target=8)
print(res)
