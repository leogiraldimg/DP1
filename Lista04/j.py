n = int(input())

entrada = input().split()
entrada = [int(i) for i in entrada]

soma = 0

for i in range(0, n):
    soma += entrada[i]

if ((soma % 3) != 0):
    print(0)
else:
    buffer = 0
    parte = soma // 3
    posicao = [0] * 500100

    i = n - 1
    while (i >= 0):
        buffer += entrada[i]

        if (buffer == parte):
            posicao[i] += 1
        i -= 1

    i = n - 2
    while (i >= 0):
        posicao[i] += posicao[i+1]
        i -= 1
    
    buffer = 0
    result = 0

    i = 0
    while (i + 2 < n):
        buffer += entrada[i]

        if (buffer == parte):
            result += posicao[i+2]

        i += 1
    
    print(result)
