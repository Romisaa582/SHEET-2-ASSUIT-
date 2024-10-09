def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

T = int(input())
for _ in range(T):
    N = int(input())
    print(factorial(N))