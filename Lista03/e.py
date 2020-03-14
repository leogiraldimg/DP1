n = int(input())
result = 0

k = 0
while (k < n):
    result += (k + 1) * (n - k) - k
    k += 1

print(result)