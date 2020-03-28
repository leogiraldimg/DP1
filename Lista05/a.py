n = int(input())
n -= 1

nomes = []
nomes.append("Sheldon")
nomes.append("Leonard")
nomes.append("Penny")
nomes.append("Rajesh")
nomes.append("Howard")

while (n >= 5):
    n = n - 5
    n = n // 2

print(nomes[n])