n = int(input())

n_decimal = 0
i = n
while i != 0:
    n_decimal += 1
    i //=10

n1 = 10**(n_decimal - 1) - 1
n2 = n - n1

result1 = 0
num = n1
while num > 0:
    result1 += num % 10
    num //= 10

result2 = 0
num = n2
while num > 0:
    result2 += num % 10
    num //= 10

print(result1 + result2)