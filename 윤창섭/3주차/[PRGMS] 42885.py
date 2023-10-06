def solution(people, limit):
    answer = 0
    people.sort(reverse = True)
    first, last = 0, len(people) - 1
    while first < last:
        if people[first] + people[last] > limit:
            first += 1
        else:
            first += 1
            last -= 1
        answer += 1
    if first == last:
        answer += 1
    return answer
