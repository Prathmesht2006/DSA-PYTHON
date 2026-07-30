# You are given an integer n. You need to check whether it is an armstrong number or not. Return true if it is an armstrong number, otherwise return false.


class Solution:
    def isArmstrong(self, n: int) -> bool:
        if n == 0:
            return True

        power = len(str(n))
        original = n
        total = 0

        while n > 0:
            digit = n % 10
            total += digit ** power
            n //= 10

        return total == original