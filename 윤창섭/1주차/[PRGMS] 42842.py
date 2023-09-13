def solution(brown, yellow):
    answer = []
    for i in range(1, yellow + 1):
        if yellow % i == 0:
            if (i + 2) * ((yellow // i) + 2) == brown + yellow:
                answer.append((yellow // i) + 2)
                answer.append(i + 2)
                break
    return answer


"""
brown은 테두리에만 존재한다.
yellow는 brown을 제외한 중앙 부분에 존재한다.
brown과 yellow의 합은 전체 카펫의 크기이다.

0 0 0 0 0 0 0 0
0 1 1 1 1 1 1 0
0 1 1 1 1 1 1 0
0 1 1 1 1 1 1 0
0 1 1 1 1 1 1 0
0 0 0 0 0 0 0 0

brown = 24, yellow = 24
brown + yellow = 48
서로 곱해 48이 되는 수를 구한다
1부터 yellow까지의 수를 i라고 할 때,
yellow % i == 0일 때의 몫이 한 줄의 yellow의 개수이다.
그리고 i + 2가 한 줄의 brown의 개수가 된다.
또한 (brown + yellow) / 한 줄의 brown의 개수가 세로의 크기가 된다.

이때, yellow의 가로의 길이 x'은 i, yellow의 세로의 길이 y'은 yellow // i가 된다.
총 직사각형의 면적인 brown + yellow 가 (x' + 2) * (y' + 2)와 같을 때, 다음 조건을 만족한다.
"""
