n  = int(input())
arr = []
for _ in range(n):
    x = set(input())
    arr.append(x)
count = set.intersection(*arr)
print(len(count))