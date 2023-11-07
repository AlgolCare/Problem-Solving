d, k = map(int, input().split())

fibonacci = [0, 1]
for i in range(d-2):
    fibonacci.append(fibonacci[-1] + fibonacci[-2])

for n in range(1, k//fibonacci[d-2] + 1):
    if (k - fibonacci[d-2] * n) % fibonacci[d-1] == 0:
        print(n)
        print((k - fibonacci[d-2] * n) // fibonacci[d-1])
        break