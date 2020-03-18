entrada = input()

if (entrada == "{}"):
    print(0)
    exit()

entrada = entrada[1:len(entrada)-1].split(", ")
arr_a = [0] * 127
result = 0

i = 0
while(i < len(entrada)):
    arr_a[ord(entrada[i])] = 1
    i += 1

i = 0
while(i < 127):
    result += arr_a[i]
    i += 1

print(result)