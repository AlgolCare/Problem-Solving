import sys; read = sys.stdin.readline

city = int(read().strip())
dist = list(map(int, read().split()))
dist.append(0)
price = list(map(int, read().split()))

now_price = 1000000000
moved = 0
result = 0

for i in range(city):
  if price[i] <now_price:
    now_price = price[i]
  result += dist[i] *now_price
print(result)