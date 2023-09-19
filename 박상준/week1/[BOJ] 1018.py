n, m = map(int, input().split())
ls = [input() for _ in range(n)]
start_w = "WBWBWBWB"
start_b = "BWBWBWBW"
cnt = 32

for i in range(n - 7):
    for j in range(m - 7):
        cnt_w = 0
        cnt_b = 0
        for k in range(8):
            for l in range(8):
                if (i + k) % 2 == 0:
                    if ls[i + k][j + l] != start_w[l]:
                        cnt_w += 1
                    if ls[i + k][j + l] != start_b[l]:
                        cnt_b += 1
                else:
                    if ls[i + k][j + l] != start_b[l]:
                        cnt_w += 1
                    if ls[i + k][j + l] != start_w[l]:
                        cnt_b += 1
        cnt = min(cnt_w, cnt_b, cnt)

print(cnt)