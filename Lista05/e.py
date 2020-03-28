n = int(input())

arr_a = input().split()
arr_a = [int(i) for i in arr_a]

arr_m = {}

for a in arr_a:
    arr_m.update({a: 0})

result = 0

for a in arr_a:
    arr_m[a] += 1
    result = max(result, arr_m[a])

print(result)