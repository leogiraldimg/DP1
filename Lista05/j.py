entrada = input().split()

n = int(entrada[0])
k = int(entrada[1])

s = input()

esquerda = 0
tamanho = 0
ct = [0] * 2

for direita in range(0, n):
    ct[ord(s[direita]) - ord("a")] += 1

    if (ct[0] <= k or ct[1] <= k):
        temp = direita - esquerda + 1
        tamanho = tamanho if (tamanho > temp) else temp
    else:
        ct[ord(s[esquerda]) - ord("a")] -= 1
        esquerda += 1

print(tamanho)