class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 1
            elif num in count:
                count[num] += 1
        appears = []
        n = len(nums)/3
        for c in count.keys():
            if count[c] > n:
                appears.append(c)
        return appears