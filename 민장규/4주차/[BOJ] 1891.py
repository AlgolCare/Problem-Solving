from math import *

N, coordinate = map(int, input().split())
dc, dr = map(int, input().split())
wordlen = len(str(coordinate))
expval = wordlen

dot = [1, 1]
for i in str(coordinate) :
    if i == '1' :
        dot[1] += int(pow(2, expval-1))
    elif i == '2' :
        pass
    elif i == '3' :
        dot[0] += int(pow(2, expval-1))
    elif i == '4' :
        dot[0] += int(pow(2, expval-1))
        dot[1] += int(pow(2, expval-1))
    expval -= 1
dot[0] -= dr
dot[1] += dc

if dot[0] <= 0 or dot[1] <= 0 or dot[0] > pow(2, wordlen) or dot[1] > pow(2, wordlen) :
    print(-1)
    exit()

r, c = [int(pow(2, wordlen-1))] * 2
expval = r // 2
result = []
for _ in range(wordlen) :
    if dot[0] <= r and dot[1] <= c :
        r -= expval
        c -= expval
        result.append('2')
    elif dot[0] > r and dot[1] <= c :
        r += expval
        c -= expval
        result.append('3')
    elif dot[0] <= r and dot[1] > c :
        r -= expval
        c += expval
        result.append('1')
    elif dot[0] > r and dot[1] > c :
        r += expval
        c += expval
        result.append('4')
    expval //= 2
print("".join(result))