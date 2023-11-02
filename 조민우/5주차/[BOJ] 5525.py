d, n = map(int, input().split())
day = []
poss = []
ans = []
cloth = []
for i in range(d):
    day.append(int(input()))
for i in range(n):
    cloth.append(list(map(int, input().split())))
for i in range(d):
    poss.append([])
    for j in range(n):
        if day[i] >= cloth[j][0] and day[i] <= cloth[j][1]:
            poss[i].append(cloth[j][2])
ans.append([0 for i in range(len(poss[0]))])
for i in range(1, len(poss)):
    ans.append([])
    for j in range(len(poss[i])):
        temp = 0
        for k in range(len(poss[i-1])):
            temp = max(abs(poss[i-1][k]-poss[i][j])+ans[i-1][k], temp)
        ans[i].append(temp)
print(max(ans[len(ans)-1]))
