class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        result = 0

        for row in nums:
            row.sort()
        
        for j in range(len(nums[0])):
            maxInCol = 0
            for i in range(len(nums)):
                maxInCol = max(maxInCol, nums[i][j])
            result += maxInCol
        return result