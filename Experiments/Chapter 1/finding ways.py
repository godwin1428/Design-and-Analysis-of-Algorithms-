def find_ways(m, n, N, start_i, start_j):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    dp = [[[0] * n for _ in range(m)] for _ in range(N + 1)]
    for k in range(1, N + 1):
        for i in range(m):
            for j in range(n):
                for direction in directions:
                    new_i, new_j = i + direction[0], j + direction[1]
                    if new_i < 0 or new_i >= m or new_j < 0 or new_j >= n:
                        dp[k][i][j] += 1
                    else:
                        dp[k][i][j] += dp[k-1][new_i][new_j]
    return dp[N][start_i][start_j]
m=2
n=2
N=2
i=0
j=0        
print(find_ways(m,n,N,i,j))
