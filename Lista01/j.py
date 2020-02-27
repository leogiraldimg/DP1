def trocaElemento(ternary, biggerElemIndex, smallerElemIndex):
    temp = ternary[smallerElemIndex]
    ternary[smallerElemIndex] = ternary[biggerElemIndex]
    ternary[biggerElemIndex] = temp
    return ternary

entrada = input()
ternary = list(entrada)

# '0' and '1' || '1' and '2'

i = 0
one = 0
ans = ""
while (i < len(ternary)):
    if (ternary[i] == "0"):
        ans = ans + "0"
    if (ternary[i] == "1"):
        one = one + 1
    if (ternary[i] == "2"):
        ans = ans + "2"
    
    i = i + 1

flag = False

i = 0
while (i < len(ans)):
    if (ans[i] == "2" and not(flag)):
        flag = True
        for x in range(one):
            print("1", end = "")
    print(ans[i], end = "")
    i = i + 1

if (not(flag)):
    for x in range(one):
        print("1", end = "")
    