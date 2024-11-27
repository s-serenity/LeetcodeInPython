from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)

        # 初始化 dp 数组
        dp = [[0] * 3 for _ in range(n)]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        dp[0][2] = 0

        # 动态规划填充 dp 数组
        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][2])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
            dp[i][2] = dp[i - 1][1] + prices[i] - fee

        # 返回最后一天的最大利润
        return max(dp[n - 1][0], dp[n - 1][1], dp[n - 1][2])


# 示例用法
solution = Solution()
prices = [1, 3, 2, 8, 4, 9]
fee = 2
print(solution.maxProfit(prices, fee))  # 输出: 8

def max_xor_sum(a, x):
    n = len(a)
    if n == 0:
        return 0

    # 初始化 dp 数组
    dp = [[0, 0, 0] for _ in range(n)]
    dp[0][0] = a[0]
    dp[0][1] = 0  # 第一个位置不能进行异或操作
    dp[0][2] = 0  # 第一个位置不能进行两次异或操作

    for i in range(1, n):
        # 不进行异或操作
        dp[i][0] = max(dp[i - 1][0] + a[i], dp[i - 1][1] + a[i], dp[i - 1][2] + a[i])

        # 进行第一次异或操作
        dp[i][1] = max(dp[i - 1][0] + int(a[i - 1] ^ x) + int(a[i] ^ x) - a[i - 1],
                       dp[i - 1][1] +a[i - 1]- int(a[i - 1] ^ x) + int(a[i] ^ x))

        # 进行第二次异或操作
        # print(dp[i - 1][1])
        # print(a[i - 1])
        # print(int(a[i - 1] ^ x))
        # print(int(a[i] ^ x))
        dp[i][2] = dp[i - 1][1] +a[i - 1]- int(a[i - 1] ^ x) + int(a[i] ^ x)

    print(dp)
    return max(dp[n - 1][0], dp[n - 1][1], dp[n - 1][2])


# 示例1
x = 2
a = [1, 1, 1]
print(max_xor_sum(a, x))  # 输出: 7

# 示例2
x = 3
a = [1, 2, 3, 4]
print(max_xor_sum(a, x))  # 输出: 14
