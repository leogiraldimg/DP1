n = int(input())
entrada = [int(a) for a in input().split()]
t = entrada[0]
i = 0

while t < n:
    i += 1
    i = i % 7
    t += entrada[i]

print(i + 1)