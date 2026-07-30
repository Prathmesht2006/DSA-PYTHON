# Given a digit d (0 to 9), find the sum of the first 50 positive integers (integers > 0) that end with digit d.


# Example 

# Input: d = 1

# Output: 12300

# Explanation:

# The first 50 positive integers ending with 1 are: 1, 11, 21, 31, ..., 491

# Their sum is 12300.



class Solution:
    def whileLoop(self, d: int) -> int:
        count = 0
        total = 0

        if d == 0:
            num = 10
        else:
            num = d

        while count < 50:
            total += num
            num += 10
            count += 1

        return total