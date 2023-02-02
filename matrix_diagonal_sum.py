class Solution(object):
    def diagonalSum(self, mat):
        is_odd_mat = False
        diagonal_sum = 0
        matrix_length = len(mat)
        if matrix_length % 2 != 0:
            mid = matrix_length//2
            is_odd_mat = True
        for index, row in enumerate(mat):
            if is_odd_mat and index == mid:
                diagonal_sum += row[index] 
            else:
                diagonal_sum += row[index] + row[-(index+1)]
        return diagonal_sum
