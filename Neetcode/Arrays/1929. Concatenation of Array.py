class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(0, n):
            nums.append(nums[i])
        return nums

    def getConcatenation2(self, nums: List[int]) -> List[int]:
        return nums * 2
