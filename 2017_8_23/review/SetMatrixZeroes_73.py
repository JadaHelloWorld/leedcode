# Given a m x n matrix, if an element is 0, set its entire row and column to 0.
#   Do it in place.


class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if matrix and len(matrix) and matrix[0]:
            n = len(matrix)
            m = len(matrix[0])

            if m:
                c = set()

                for i in range(n):
                    row = False
                    for j in range(m):
                        if matrix[i][j] == 0:
                            c.add(j)
                            row = True
                    if row:
                        # for j in range(m):
                        matrix[i] = [0] * m

                for j in c:
                    for i in range(n):
                        matrix[i][j] = 0

