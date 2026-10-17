
class Solution(object):
    def setZeroes(self, matrix):
        rows = set()
        cols = set()

        m = len(matrix)
        n = len(matrix[0])

        # Step 1: Find all zeros
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)

        # Step 2: Set corresponding rows and columns to zero
        for i in range(m):
            for j in range(n):
                if i in rows or j in cols:
                    matrix[i][j] = 0
