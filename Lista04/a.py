n = int(input())
arr_n = input().split()
arr_n = [int(i) for i in arr_n]
par = 0
ultimoPar = 0
ultimoImpar = 0

i = 1
while(i <= n):
    if (arr_n[i - 1] % 2 == 0):
        par += 1
        ultimoPar = i
    else:
        par -= 1
        ultimoImpar = i
    i += 1

result = (ultimoImpar if par > 0 else ultimoPar)
print(result)