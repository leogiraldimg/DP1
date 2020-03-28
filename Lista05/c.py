class xa:
    def __init__(self, x, a):
        self.x = x
        self.a = a

n = int(input())

macas = []
posicao = 0
negativo = 0
total = 0

for i in range(0, n):
    entrada = input().split()

    x = int(entrada[0])
    a = int(entrada[1])

    macas.append(xa(x, a))

    if (x > 0):
        posicao += 1
    else:
        negativo += 1
    
    total += a

macas.sort(key=lambda x: x.x)

if (posicao < negativo - 1):
    for p in range(0, negativo - 1 - posicao):
        total -= macas[p].a
else:
    if (negativo < posicao - 1):
        for p in range(0, posicao - 1 - negativo):
            total -= macas[n - 1 - p].a

print(total)