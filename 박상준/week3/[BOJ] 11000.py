import heapq
import sys

input = sys.stdin.readline

n = int(input())

lectures = [list(map(int, input().split())) for _ in range(n)]
rooms = []
lectures.sort()
heapq.heappush(rooms, lectures[0][1]) # 강의실에는 이전 강의 끝나는 시간만 저장, 최소힙 사용해서 순서 보장

for i in range(1, n):
    if lectures[i][0] < rooms[0]: # 강의실 끝나는 시간이 현재 강의 시작 시간보다 늦으면 
        heapq.heappush(rooms, lectures[i][1]) # 강의실 새로 개설
    else: # if문 False이면 강의실 마지막 강의시간 업데이트
        heapq.heappop(rooms) # 현재 강의실 강의 끝나는 시간 삭제 후
        heapq.heappush(rooms, lectures[i][1]) # 새 강의시간 입력

print(len(rooms))