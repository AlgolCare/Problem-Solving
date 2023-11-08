"""
1번 예제를 확인해보면 다음과 같은 표를 그릴 수 있다.
여기서 행은 날짜를 의미하며, 열은 몇 번째 옷인지를 의미한다.

   0(30)   1(90)   2(60)   3(40)
1   x(0)    x(0)    o(0)    o(0) 
2   x       o(50)   o(20)   x
3   x       x       o(80)   x
3번옷 -> 1번옷 -> 2번옷 순서대로 입었을 때, 화려함의 수치가 가장 높은 것을 알 수 있다.
dp[날짜][옷 종류] = max(dp[날짜][옷 종류], dp[날짜 - 1][그 날 입은옷 종류] + |오늘 옷 점수 - 그 날 옷 점수|) 의 점화식을 구현하면 해결된다.
"""

import sys
from collections import defaultdict

def read_line():
    return sys.stdin.readline()

d, n = map(int, read_line().split())
max_temp = [int(read_line()) for i in range(d)]

scores = dict()
clothes = list()
for cloth in range(n):
    low, high, score = map(int, read_line().split())
    scores[score] = cloth # 점수를 key, 몇 번째 옷인지를 value에 입력
    clothes.append((low, high, score))

dp = [[0] * n for i in range(d)]

wear = defaultdict(list)

for day in range(d):
    temp = max_temp[day]
    for cloth in range(n):
        low, high, score = clothes[cloth]
        if low <= temp <= high:
            wear[day].append(score) # 조건에 맞는 경우 해당 날짜에 대한 입을 수 있는 옷 모두 삽입

for today in range(1, d):
    for today_score in wear[today]:
        today_cloth = scores[today_score]
        for yesterday_score in wear[today - 1]:
            yesterday_cloth = scores[yesterday_score]
            dp[today][today_cloth] = max(dp[today][today_cloth], dp[today - 1][yesterday_cloth] + abs(today_score - yesterday_score))

print(max(dp[-1]))
