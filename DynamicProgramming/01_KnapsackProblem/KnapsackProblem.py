class Solution():
    def do(self, list_weights, list_values, total_weight):
        '''
        dp[i][j] = 
                    if list_weights[i] > j:
                        dp[i - 1][j]
                    else:
                        max(list_values[i] + dp[i - 1][j - list_weights[i]], dp[i - 1][j])
        '''
        dp = [[0] * (total_weight + 1) for _ in range(len(list_weights))]
        for i in range(len(list_weights)):
            for j in range(total_weight + 1):
                if j == 0:
                    continue

                if i == 0:
                    if list_weights[i] > total_weight:
                        continue
                    dp[i][j] = list_values[i]
                else:
                    if list_weights[i] > j:
                        dp[i][j] = dp[i - 1][j]
                    else:
                        dp[i][j] = max(list_values[i] + dp[i - 1][j - list_weights[i]], dp[i - 1][j])
        return dp[-1][-1]



solution = Solution()
print solution.do([1, 3, 4, 5], [1, 4, 5, 7], 7)
