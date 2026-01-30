class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        counter = 0
        nums.sort()
        highest = nums[-1]
        for i, num in enumerate(nums):
            if num != counter:
                return counter

            counter = counter + 1
        return counter