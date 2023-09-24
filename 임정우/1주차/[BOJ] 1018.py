def cal_min(ny, nx):
    w_cnt = 0
    b_cnt = 0
    for y in range(i, i + 8):
        for x in range(j, j+ 8):
            if ((y + x) % 2 == 0): # 짝수인 경우 -> 시작점과 같아야함
                if (map[y][x] == 'W'): #시작점이 W, 현재 위치가 B인 경우에 cnt 증가
                    b_cnt+=1
                else: #시작점이 B, 현재 위치가 W인 경우에 cnt 증가
                    w_cnt+=1
            else: # 홀수인 경우 -> 시작점과 달라야함
                if (map[y][x] == 'W'):
                    w_cnt+=1
                else :
                    b_cnt+=1
    return min(b_cnt, w_cnt)
sizeY, sizeX = map(int, input().split())
map = (list((input()) for _ in range(sizeY)))
ans = 987654321
for i in range(sizeY - 7):
    for j in range(sizeX - 7):
        ans = min(ans, cal_min(i, j))
print(ans)