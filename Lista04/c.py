import math

entrada = input().split()

n = int(entrada[0])
k = int(entrada[1])

amazon = [0] * (n + 1)

amazon[0] = 0
amazon[1] = 0

i = 2
while(i <= n):
    amazon[i] = 1
    i += 1

i = 2
while(i <= (math.sqrt(n) + 1)):
    if (amazon[i] == 0):
        i += 1
        continue

    m = 2 * i
    while(m <= n):
        amazon[m] = 0
        m += i

    i += 1

netflix = []
i = 2
while(i <= n):
    if (amazon[i] != 0):
        netflix.append(i)
    i += 1

result = 0
i = 2
while(i < len(netflix)):
    m = 0
    while(m < (i - 1)):
        if((netflix[m] + netflix[m + 1] + 1) == netflix[i]):
            result += 1
        m += 1

    i += 1

if (result >= k):
    print("YES")
else:
    print("NO")