class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        solution = 0
        segment = []
        for n in nums:
            while segment and segment[-1] > n:
                segment.pop()
            if n > 0 and (not segment or n != segment[-1]):
                solution += 1
                segment.append(n)
        return solution
