def findxy(n, i, x, y):
    global d
    if i == d:
        return x, y
    else:
        if n % 10 == 1:
            return findxy(n // 10, i+1, x, y + 2**i)
        elif n % 10 == 2:
            return findxy(n // 10, i+1, x, y)
        elif n % 10 == 3:
            return findxy(n // 10, i+1, x + 2 ** i, y)
        elif n % 10 == 4:
            return findxy(n // 10, i+1, x + 2**i, y + 2**i)

def findnum(x, y, i, num):
    global d
    if (i == d+1):
        return num
    t = 2 ** (d - i)
    num *= 10
    if x >= t and y >= t:
        return findnum(x-t, y-t, i+1, num+4)
    elif x >= t:
        return findnum(x-t, y, i+1, num+3)
    elif y >= t:
        return findnum(x, y-t, i+1, num+1)
    else:
        return findnum(x, y, i+1, num+2)
d, n = map(int, input().split())
x, y = map(int, input().split())
findx, findy = findxy(n, 0, 0, 0)
findx -= y
findy += x
if findx < 0 or findy >= 2**d:
    print(-1)
else:
    print(findnum(findx,findy,1,0))