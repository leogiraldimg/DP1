def generateRounding(num1, num2):
    rounding = num1 if num2 == 0 else generateRounding(num2, (num1 % num2))
    return rounding

entrada = input().split()
entrada = [int(i) for i in entrada]

n = entrada[0]
k = entrada[1]

tmp = 1
p = 0
while(p < k):
    tmp *= 10
    p += 1

rounding = generateRounding(tmp, n)

result = (n // rounding) * tmp
print(result)