class Solution():
    def do(self, str1, str2):
        len_str1, len_str2 = len(str1), len(str2)
        dp = [[0] * (len_str1 + 1) for _ in range(len_str2 + 1)]
        '''
        dp[i][j] = 
                    max(dp[i - 1][j], dp[i][j - 1]) if str1[j] != str2[i]
                    dp[i - 1][j - 1] + 1 if str1[j] == str2[i]
        '''
        for i in range(1, len_str2 + 1):
            for j in range(1, len_str1 + 1):
                if str1[j - 1] == str2[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]

solution = Solution()
print solution.do('abcdef', 'acbcf')
print solution.do('abcdca', 'acbc')
