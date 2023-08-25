class Solution:

    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeSort(nums, s, e):
            # check if
            if (e - s + 1) <= 1:
                return nums

            m = (e + s) // 2

            mergeSort(nums, s, m)  # sort left side
            mergeSort(nums, m + 1, e)  # sort right side
            merge(nums, s, m, e)  # merge sides together

            return nums

        def merge(nums, s, m, e):
            # split arrays
            L = nums[s: m + 1]
            R = nums[m + 1: e + 1]

            i = 0  # index for L
            j = 0  # index for R
            k = s  # index for nums

            # merge two sorted halves into the original array
            while i < len(L) and j < len(R):
                if L[i] <= R[j]:
                    nums[k] = L[i]
                    i += 1
                else:
                    nums[k] = R[j]
                    j += 1
                k += 1

            # handle when one array has elements left
            while i < len(L):
                nums[k] = L[i]
                i += 1
                k += 1

            while j < len(R):
                nums[k] = R[j]
                j += 1
                k += 1

        return mergeSort(nums, 0, len(nums) - 1)