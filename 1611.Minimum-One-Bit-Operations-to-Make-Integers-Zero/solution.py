class Solution(object):
    def minimumOneBitOperations(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0

        k = 0 
        while 2 ** k <= n:
            k += 1
       

        return 2 ** k - 1 - self.minimumOneBitOperations(2 ** (k - 1) ^ n)
