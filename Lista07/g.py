entrada = input().split()
n = int(entrada[0])
k = int(entrada[1])

arr_result = []
k_temp = k
n_temp = n
soma = 0
m = 0

i = 30
while i >= 0 and k >= 0:
    m = 1 << i
    if (m > n) or (n - m < k - 1):
        i -= 1
        continue
    soma += m
    arr_result.append(m)
    n -= m
    k -= 1

if (len(arr_result) == k_temp and soma == n_temp):
    print("YES")

    for resp in arr_result:
        print(resp, end=" ")
    print("")
else:
    print("NO")