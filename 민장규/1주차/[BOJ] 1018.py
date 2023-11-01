r, c = map(int, input().split())
arr = [list(input()) for _ in range(r)]

def reverse(c) :
    if c == "B" :
        return "W"
    else :
        return "B"

def count(text) :
    result = 100000000
    for i in range(r-7) :
        for j in range(c-7) :
            cnt = 0
            chess = [row[j:j+8] for row in arr[i:i+8]]
            for R in range(8) :
                text = reverse(text)
                for C in range(8) :
                    if chess[R][C] != text :
                        cnt += 1
                    text = reverse(text)
            result = min(result, cnt)
    return result

print(min(count(reverse(arr[0][0])), count(arr[0][0])))