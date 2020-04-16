entrada = input().split()
n = int(entrada[0])
L = int(entrada[1])
arr_c = [int(c) for c in input().split()]

for i in range(0, n - 1):
    arr_c[i + 1] = min(arr_c[i + 1], 2 * arr_c[i])

result = 4*(10**18)
soma = 0

i = n - 1
while i >= 0:
    temp = L // (1 << i)
    soma += temp * arr_c[i]
    L -= temp << i
    result = min(result, soma + (L > 0) * arr_c[i])
    i -= 1

print(result)