arr_entrada = []
for i in range(0, 3):
    arr_entrada.append(input())

rounds = [[0,0,0],[0,0,0],[0,0,0]]
results = [[True,True,True],[True,True,True],[True,True,True]]

for i in range(0 ,3):
    for j in range(0, 3):
        rounds[i][j] = int(arr_entrada[i].split()[j])

if (rounds[0][0]%2 != 0):
    results[0][0] = not(results[0][0])
    results[1][0] = not(results[1][0])
    results[0][1] = not(results[0][1])

if (rounds[1][0]%2 != 0):
    results[0][0] = not(results[0][0])
    results[1][0] = not(results[1][0])
    results[2][0] = not(results[2][0])
    results[1][1] = not(results[1][1])
if (rounds[2][0]%2 != 0):
    results[2][0] = not(results[2][0])
    results[2][1] = not(results[2][1])
    results[1][0] = not(results[1][0])
if (rounds[0][1]%2 != 0):
    results[0][0] = not(results[0][0])
    results[0][1] = not(results[0][1])
    results[1][1] = not(results[1][1])
    results[0][2] = not(results[0][2])
if (rounds[1][1]%2 != 0):
    results[1][1] = not(results[1][1])
    results[0][1] = not(results[0][1])
    results[2][1] = not(results[2][1])
    results[1][0] = not(results[1][0])
    results[1][2] = not(results[1][2])
if (rounds[2][1]%2 != 0):
    results[1][1] = not(results[1][1])
    results[2][0] = not(results[2][0])
    results[2][1] = not(results[2][1])
    results[2][2] = not(results[2][2])
if (rounds[0][2]%2 != 0):
    results[0][1] = not(results[0][1])
    results[0][2] = not(results[0][2])
    results[1][2] = not(results[1][2])
if (rounds[1][2]%2 != 0):
    results[0][2] = not(results[0][2])
    results[1][1] = not(results[1][1])
    results[1][2] = not(results[1][2])
    results[2][2] = not(results[2][2])
if (rounds[2][2]%2 != 0):
    results[2][2] = not(results[2][2])
    results[2][1] = not(results[2][1])
    results[1][2] = not(results[1][2])

i = 0
while (i < 3):
    j = 0
    while (j < 3):
        if (results[i][j] == True):
            print(1, end="")
        else:
            print(0, end="")
        j += 1
    print("")
    i += 1