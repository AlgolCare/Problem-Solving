NO = -1
D, N = map(int, input().split())
T = [int(input()) for _ in range(D)]
C = [list(map(int, input().split())) for _ in range(N)]
dp = [[NO for _ in range(5)] for _ in range(5)]

for i in range(len(C)) :
    if C[i][0] <= T[0] and T[0] <= C[i][1] :
        dp[i][0] = [C[i][2] ,0]

for i in range(1, D) :
    for j in range(len(C)) :
        if C[j][0] <= T[i] and T[i] <= C[j][1] :
            dp[j][i] = [0, 0]
            for k in range(len(C)) :
                if dp[k][i-1] != NO :
                    if dp[j][i][0] <= abs(C[j][2] - C[k][2]) :
                        dp[j][i] = [abs(C[j][2] - C[k][2]), dp[k][i-1][1] + abs(C[j][2] - C[k][2])]
          

for row in dp :
    print(row)          
              
result = 0
for i in range(len(C)) :
    if dp[i][D-1] != NO and result <= dp[i][D-1][1] :
        result = dp[i][D-1][1]
print(result)