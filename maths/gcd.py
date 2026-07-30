# You are given two integers n1 and n2. You need find the Greatest Common Divisor (GCD) of the two given numbers. Return the GCD of the two numbers.

class Solution:
    def GCD(self, n1, n2):


        # ans = 1
        # for i in range(1, min(n1, n2) + 1):
        #     if n1 % i == 0 and n2 % i == 0:
        #         ans = i
        # return ans


        while n2:
            n1,n2=n2,n1%n2
        return n1


    