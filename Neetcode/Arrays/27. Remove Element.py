class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        pos = 0
        for i in range(pos, len(nums)):
            if nums[i] != val:
                nums[pos] = nums[i]
                pos += 1

        return pos