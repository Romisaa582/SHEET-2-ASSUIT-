symbol = input()
n = int(input())
numbers = [int(x) for x in input().split()]
 
for num in numbers:
    print(symbol * num)