D, K = map(int, input().split())

for i in range(1, 100000):

    for j in range(1, 100000):
        dp = [0] * (D + 1)
        dp[0] = i
        dp[1] = j

        for l in range(2, D + 1):
            dp[l] = dp[l - 1] + dp[l - 2]

        if dp[-1] == K:
            print(dp[1])
            print(dp[2])
            exit()
        