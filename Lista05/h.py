entrada = input()

n = int(entrada.split()[0])
m = int(entrada.split()[1])

result = m if (m < n) else n

print(result + 1)

k = result
while(k >= 0):
    print(result - k, end=" ")
    print(k)

    k -= 1