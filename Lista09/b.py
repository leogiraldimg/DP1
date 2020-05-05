import math

entrada = input().split()

r = int(entrada[0])
x1 = int(entrada[1])
y1 = int(entrada[2])
x2 = int(entrada[3])
y2 = int(entrada[4])

d = math.sqrt(pow(y2 - y1, 2) + pow(x2 - x1, 2))

print(math.ceil(d / r / 2))