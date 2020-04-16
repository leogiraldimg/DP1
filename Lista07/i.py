n = int(input())

arr_l = []
arr_r = []
for i in range(0, n):
    entrada = input().split()
    arr_l.append(int(entrada[0]))
    arr_r.append(int(entrada[1]))

result = n

arr_l.sort()
arr_r.sort()

i = 0
while i < n:
    result += max(arr_l[i], arr_r[i])
    i += 1

print(result)