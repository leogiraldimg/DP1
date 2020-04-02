import math

def digitosEmComum(a, b):
    digitos = [0] * 10
    result = 0

    while(a > 0):
        digitos[a % 10] = 1
        a = a // 10
    
    while(b > 0):
        if (digitos[b % 10] != 0):
            result = 1
            break
        b = b // 10
    
    return result

n = int(input())
total = 0

divisores = []

i = 1
while(i <= math.sqrt(n)):
    if(n % i == 0):
        divisores.append(i)
        if (n / i > i):
            divisores.append(n // i)
    i += 1

for i in range(0, len(divisores)):
    if (digitosEmComum(n, divisores[i]) == 1):
        total += 1

print(total)