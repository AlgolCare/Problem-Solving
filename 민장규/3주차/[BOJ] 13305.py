N = int(input())
road = list(map(int, input().split()))
oil = list(map(int, input().split()))

def cost(index) :
    cnt = oil[index]
    while index < len(oil)-1 and oil[index] >= cnt :
        index += 1
    return index

index = 0
result = 0
while True :
    km = 0
    cnt = cost(index)
    for i in range(index, cnt) :
        km += road[i]        
    result += oil[index] * km
    index = cost(index)
    if index == len(oil)-1 :
        break
print(result)