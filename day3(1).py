def maxProfit(prices):
    n = len(prices)
    if n < 2:
        return 0
    dp = [0] * n
    for i in range(1, n):
        max_profit = 0
        for j in range(i):
            max_profit = max(max_profit, prices[i] - prices[j] + dp[j-1])
        dp[i] = max(dp[i-1], max_profit)
    return dp[-1]

prices = [7, 6, 4, 3, 1]
print(maxProfit(prices))
