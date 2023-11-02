d, k = map(int, input().split())
dp = [[1, 0], [0, 1]]
for i in range(2, d):
    dp.append([dp[i-2][0]+dp[i-1][0], dp[i-2][1]+dp[i-1][1]])
first, second = dp[d-1][0], dp[d-1][1]
for i in range(first, k, first):
    if ((k - i) % second == 0):
        print(i // first)
        print((k-i) // second)
        exit()