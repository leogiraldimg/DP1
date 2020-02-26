entrada = input()
n = int(entrada.split(" ")[0]) # number of available stages
k = int(entrada.split(" ")[1]) # number of stages to use in the rocket

stages = input()

alphabet = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11, "l": 12, "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21, "v": 22, "w": 23, "x": 24, "y": 25, "z": 26}

stages = list(stages)
stages.sort()

cnt = alphabet[stages[0]]
k = k - 1
j = 0
i = 1
while (i < n):
    if (k <= 0):
        break

    if (alphabet[stages[i]]-alphabet[stages[j]] >= 2):
        cnt += (alphabet[stages[i]])
        k = k - 1
        j = i
    i = i + 1

if (k <= 0):
    print(cnt)
else:
    print("-1")