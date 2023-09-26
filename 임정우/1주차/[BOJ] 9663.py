size = int(input())
visited = [-1] * size
cnt = 0
def check_position(chess_pos):
    for i in range(chess_pos):
        if (visited[chess_pos] == visited[i] or chess_pos - i == abs(visited[chess_pos] - visited[i])):
            return False
    return True

def try_position(chess_pos):
    global size, cnt
    if (chess_pos == size): ## 제시된 개수 모두 채운 상황
        cnt+=1
        return 
    for i in range(size): 
        visited[chess_pos] = i ## 일단 놓아보기
        if (check_position(chess_pos)): ## 겹치지 않는 위치인지 확인 맞다면 다음 기물, 아니면 현재 기물 바꾸기
            try_position(chess_pos+1)

try_position(0)
print(cnt)