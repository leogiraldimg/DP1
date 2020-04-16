n = int(input())
arr_a = input().split()
arr_a = [int(a) for a in arr_a]

result = 0
agora = 0
ct = 0
j = 0

for i in range(0, n):
    if (arr_a[i] == 1):
        ct += 1
        if (ct == 1):
            result = 1
        else:
            result *= i - j
        j = i

print(result)