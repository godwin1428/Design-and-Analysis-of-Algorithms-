def knap(val, wei, cap):
    n = len(val)
    dp = [[0 for _ in range(cap + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(1, cap + 1):
            if wei[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - wei[i - 1]] + val[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]
    return dp[n][cap]
val = [1,4,5, 7]
wei = [1,3,4,5]
cap = 7
mx = knap(val, wei, cap)
print(f"The maximum value {cap} is {mx}")
