entrada = input()

n = int(entrada.split()[0])
k = int(entrada.split()[1])

result = (k + n - 1) // n
print(result)