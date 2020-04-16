import math

n = int(input())

result = 0
flag = False

i = 2
while (i < math.sqrt(n) + 1):
    if (n % i == 0):
        flag = True
        n -= i
        result += 1
        break
    i += 1

if flag:
    result += n // 2
else:
    result = 1

print(result)