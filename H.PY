def is_prime(X):
    if X < 2:
        return "NO"
    for i in range(2, X):
        if X % i == 0:
            return "NO"
    return "YES"

# Example usage
X = int(input())
print(is_prime(X))