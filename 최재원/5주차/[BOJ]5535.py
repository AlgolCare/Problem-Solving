D, N = map(int, input().split())
T = [int(input()) for _ in range(D)]
clothes = []

for _ in range(N):
    a, b, c = map(int, input().split())
    clothes.append((a, b, c))

dp = [[0] * N for _ in range(D)]

for i in range(1, D):
    for j in range(N):
        for k in range(N):
            if clothes[j][0] <= T[i] <= clothes[j][1]:
                dp[i][j] = max(dp[i][j], dp[i-1][k] + abs(clothes[j][2] - clothes[k][2]))

result = max(dp[D-1])

print(result)
