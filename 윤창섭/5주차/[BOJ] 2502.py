"""
예제
6 41

첫날 A, 둘째날 B
1 A
2 B
3 A + B
4 A + 2B
5 2A + 3B
6 3A + 5B
-> Fibonacci

D만큼 Fibonacci를 구한 뒤 D 번째에 있는 값과 K를 비교하며 A와 B값을 조절해줌

예시 1번
1 1 2 3 5 8 
1 2 3 5 8 13
2 3 5 8 13 21
3 4 7 11 18 29
4 5 9 14 23 37
5 6 11 17 28 43
4 6 10 16 26 42
3 6 9 15 24 39
6 7 13 20 33 53
5 7 12 19 31 50
4 7 11 18 29 47
3 7 10 17 27 44
2 7 9 16 25 41
"""

import sys

def read_line():
    return sys.stdin.readline()

d, k = map(int, read_line().split())

dp = [0 for i in range(d)]
dp[0], dp[1] = 1, 1

while (True):
    for i in range(2, d):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    if dp[d - 1] == k: # 같을 경우 break
        print(dp[0])
        print(dp[1])
        break
    elif dp[d - 1] < k: # 작을 경우 A와 B의 차이를 크게
        dp[0] = dp[1]
        dp[1] += 1
    else: # 클 경우 A와 B의 차이를 작게
        dp[0] -= 1
