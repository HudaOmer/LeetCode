class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)
        prefix = [0] * n
        prefix[0] = nums[0]

        for i in range(1, n):
            prefix[i] = nums[i] + prefix[i - 1]

        for i in range(n - 2, -1, -1):
            nums[i] = nums[i] + nums[i + 1]

        for i in range(n):
            if nums[i] == prefix[i]:
                return i

        return -1
