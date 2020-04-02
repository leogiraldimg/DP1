entrada1 = input().split()
n = int(entrada1[0])
m = int(entrada1[1])

entradan = input().split()
arr_a = [int(a) for a in entradan]

arr_aa = [0] * 100010

i = 1
for a in arr_a:
    arr_aa[i] = arr_aa[i - 1] + a

    i += 1

arr_result = []

i = 0
while(i < m):
    entradaab = input().split()
    a = int(entradaab[0])
    b = int(entradaab[1])

    calvin = arr_aa[b] - arr_aa[a - 1]

    if (calvin % 2 == 0):
        arr_result.append("Sim")
    else:
        arr_result.append("Nao")
    
    i += 1

for result in arr_result:
    print(result)