k = int(input())
x, y = map(int, input().split())
real_x = x - 1
real_y = 2**k - y
floor = [[0] * (2 ** k) for _ in range(2 ** k)]
floor[real_x][real_y] = -1

def check():
    pass

def fill():
    pass

number = 0

for f in floor:
    print(" ".join(map(str, f)))
