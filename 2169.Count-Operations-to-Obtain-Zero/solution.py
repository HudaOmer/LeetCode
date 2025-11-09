class Solution(object):
    def countOperations(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        if not (num1 and num2):
            return 0
        if num1 >= num2:
            num1 -= num2
            return 1 +  self.countOperations(num1, num2)
        else:
            num2 -= num1
            return 1 + self.countOperations(num1, num2)
