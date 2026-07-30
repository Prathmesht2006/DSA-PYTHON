# You are given an integer n. Return the integer formed by placing the digits of n in reverse order.

class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        sign = -1 if x < 0 else 1
        x = abs(x)

        while x != 0:
            digit = x % 10
            x //= 10

            # Overflow check
            if rev > (2**31 - 1) // 10 or (
                rev == (2**31 - 1) // 10 and digit > 7
            ):
                return 0

            rev = rev * 10 + digit

        return sign * rev