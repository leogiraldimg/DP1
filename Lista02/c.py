config = input()
n = int(config.split(" ")[0])
k = int(config.split(" ")[1])
entrada = input()

alphabet = [0] * k

i = 0
while (i < len(entrada)):
    l = ord(entrada[i]) - ord("A")
    if (l < k):
        alphabet[l] = alphabet[l] + 1
    i = i + 1
    
result = n
i = 0
while (i < k):
    result = min(result, alphabet[i])
    i = i + 1

print(result*k)