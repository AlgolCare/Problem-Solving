d, n = map(int, input().split())

temp = [int(input()) for _ in range(d)]
clothes = [list(map(int, input().split())) for _ in range(n)]

dp = [[0 for _ in range(n)] for __ in range(d)]

for i in range(1, d):
    for j in range(n):
        if clothes[j][0] <= temp[i] <= clothes[j][1]: # 입을 수 있으면
            dp[i][j] = dp[i-1][j] + clothes[j][2]


print(dp)