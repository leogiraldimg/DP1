n = int(input())
entrada = input().split()
arr_a = [int(a) for a in entrada]

result = 0
temp = 0

for i in range(0, n):
    temp = 0
    for j in range(i, n):
        temp = temp ^ arr_a[j]
        result = max(result, temp)

print(result)