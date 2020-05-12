n = int(input())
entrada = input()

temp1 = 0
temp2 = 0

for i in range(len(entrada)):
    if entrada[i] == '0':
        temp1 += 1
    else:
        temp2 += 1

partial = min(temp1, temp2)
result = n - (2 * partial)
print(result)