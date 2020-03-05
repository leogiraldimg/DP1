import math

entrada = input()

area1 = int(entrada.split(" ")[0])
area2 = int(entrada.split(" ")[1])
area3 = int(entrada.split(" ")[2])

aresta1 = math.sqrt((area1 * area2) / area3)
aresta2 = math.sqrt((area3 * area1) / area2)
aresta3 = math.sqrt((area3 * area2) / area1)

resultado = aresta1 + aresta2 + aresta3

print(int(resultado * 4))