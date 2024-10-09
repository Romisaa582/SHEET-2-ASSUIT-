a, b = map(int, input().split())
 
def is_lucky(n):
    for digit in str(n):
        if digit not in ['4', '7']:
            return False
    return True
 
lucky_numbers = []
for i in range(a, b+1):
    if is_lucky(i):
        lucky_numbers.append(i)
 
if not lucky_numbers:
    print(-1)
else:
    print(' '.join(map(str, lucky_numbers)))