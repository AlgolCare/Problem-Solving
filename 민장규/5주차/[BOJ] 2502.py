def callzero() :
    global zero
    zero += 1

def callone() :
    global one
    one += 1

def fibonacci(n) :
    global zero, one, fib, lst
    
    if n < 0 :
        return
    if fib[n] != -1 :
        lst[0] += fib[n][0]
        lst[1] += fib[n][1]
        return
    
    if n == 0 :
        callzero()
    if n == 1 :
        callone()
    if n > 1 :
        fibonacci(n-1)
        fibonacci(n-2)
    
    lst[0] += zero
    lst[1] += one
    fib[n] = lst.copy()

result = []
fib = [-1 for _ in range(30)]
for i in range(30) :
    zero = 0
    one = 0
    lst = [0, 0]
    fibonacci(i)

D, K = map(int, input().split())
A = fib[D-1][0]
B = fib[D-1][1]

for i in range(K//A) :
    for j in range(K//B) :
        if A*i + B*j == K :
            print(i)
            print(j)
            exit()