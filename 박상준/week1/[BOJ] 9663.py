count = 0 
N = int(input())
visited = [0] * (N)

def check(x):
    for i in range(x):
        if visited[x] == visited[i] or abs(visited[x] - visited[i]) == x - i:
            return False
    return True


def queen(x):
    global count
    if x == N:
        count += 1
    else:
        for i in range(N):
            visited[x] = i
            if check(x):
                queen(x+1)

queen(0)
print(count)