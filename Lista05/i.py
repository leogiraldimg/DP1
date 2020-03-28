n = int(input())
arr_a = input().split()
arr_a = [int(a) for a in arr_a]
dicionario = dict()

for a in arr_a:
    dicionario[a] = dicionario.get(a-1, 0) + 1

comeco = 0
final = 0
result = 0
for k in dicionario.keys():
    if (dicionario[k] > result):
        result = dicionario[k]
        final = k
        comeco = k - dicionario[k] + 1

print(result)

atual = comeco
arr_result = []
for i, x in enumerate(arr_a):
    if (atual == x):
        arr_result.append(i + 1)
        atual += 1;

for i in range(0, len(arr_result)):
    if (i == len(arr_result) - 1):
        print(arr_result[i])
    else:
        print(arr_result[i], end=' ')