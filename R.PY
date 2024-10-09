while True:
    try:
        N, M = map(int, input().split())
        if N <= 0 or M <= 0:
            break
 
        result = []
        for num in range(min(N, M), max(N, M) + 1):
            result.append(str(num))
        total = sum(range(min(N, M), max(N, M) + 1))
        print(" ".join(result) + f" sum ={total}")
    except ValueError:
        break