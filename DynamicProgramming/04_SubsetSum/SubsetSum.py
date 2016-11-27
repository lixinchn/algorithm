class Solution():
    def do(self, arr_input, sum_num):
        len_arr = len(arr_input)
        dp = [[True] * (sum_num + 1) for _ in range(len_arr)]
        for i in range(len_arr):
            for j in range(1, sum_num + 1):
                if i == 0:
                    if arr_input[i] != j :
                        dp[i][j] = False
                else:
                    if arr_input[i] > j:
                        dp[i][j] = dp[i - 1][j]
                    else:
                        dp[i][j] = dp[i - 1][j] or dp[i - 1][j - arr_input[i]]
        return dp[-1][-1]

solution = Solution()
print solution.do([2, 3, 7, 8, 10], 11)
