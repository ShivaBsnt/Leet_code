class Solution(object):
    def pivotInteger(self, n):
        n_list = list(range(n+1))
        left_sum = 0
        total_sum = sum(n_list)

        for index, elem in enumerate(n_list):
            pivot_elem = elem
            left_sum = sum(n_list[:index])
            right_sum = total_sum - left_sum - pivot_elem
            if left_sum == right_sum:
                return elem
                
        return -1