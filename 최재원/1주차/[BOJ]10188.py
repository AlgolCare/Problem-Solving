N, M = map(int, input().split())

AnswerBoard=[['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], \
            ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], \
            ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], \
            ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], \
            ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], \
            ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], \
            ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], \
            ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']] 

행 = N #행, 가로
열 = M #열, 세로
max = 0
min = 64
ans = 0
board = [list(map(str, input())) for _ in range(N)]
    
for i in range(열-7):
    for j in range(행-7):
        cnt = 0
        for k in range(8):
            for l in range(8):
                if AnswerBoard[k][l] != board[k+j][l+i]:
                    cnt += 1
        if cnt < min:
            min = cnt
        if max < cnt:
            max = cnt
if 8*8-max>min :
    ans=min
else : 
    ans=8*8-max

print(ans)