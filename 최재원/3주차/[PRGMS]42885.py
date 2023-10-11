def solution(people, limit):
    people.sort()
    result = 0
    start = 0
    end = len(people) -1
    
    while start <= end :
        if people[start] + people[end] <= limit :
            start += 1
            end -= 1
        else :
            end -= 1
        result += 1
    return result

print(solution([70, 80, 50, 50], 100))