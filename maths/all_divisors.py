# You are given an integer n. You need to find all the divisors of n. Return all the divisors of n as an array or list in a sorted order.

class Solution:
    def divisors(self, n: int) -> list[int]:
        ans = []

        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                ans.append(i)

                if i != n // i:
                    ans.append(n // i)

        ans.sort()
        return ans