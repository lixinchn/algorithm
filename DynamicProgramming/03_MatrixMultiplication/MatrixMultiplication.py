# -*- coding: utf-8 -*- 


class Solution():
    def do(self, arr_matrix):
        '''
        鉴于矩阵的乘法必须遵循的性质，所以输入这里做了简化。
        arr_matrix[0], arr_matrix[1] 代表第一个矩阵的维度
        arr_matrix[1], arr_matrix[2] 代表第二个矩阵的维度
        依次类推
        '''
        len_matrix = len(arr_matrix) - 1
        dp = [[0] * len_matrix for _ in range(len_matrix)]
        for i in range(1, len_matrix):
            for j in range(len_matrix):
                if j + i >= len_matrix:
                    break
                dp[j][j + i] = 100000000000
                k = j + 1
                while k <= i + j:
                    temp = arr_matrix[j] * arr_matrix[k] * arr_matrix[j + i + 1] + \
                            dp[j][k - 1] + \
                            dp[k][i + j]
                    if temp < dp[j][j + i]:
                        dp[j][j + i] = temp
                    k += 1

        return dp[0][-1]

solution = Solution()
print solution.do([2,3,6,4,5])